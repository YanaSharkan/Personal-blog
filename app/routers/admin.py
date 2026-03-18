from fastapi import APIRouter, Request, Depends, Form, HTTPException, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from ..dependencies import admin_auth
from ..services.articles_services import get_articles, get_article_by_id, add_article, update_article, delete_article
from ..services.admin_services import is_password_set, set_password, validate_password

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/admin/articles", response_class=HTMLResponse, dependencies=[Depends(admin_auth)])
def admin_dashboard(
        request: Request,
        page: int = Query(1, ge=1),
        size: int = Query(5, ge=1, le=100)
):
    articles = get_articles()
    total = len(articles)
    start = (page - 1) * size
    end = start + size
    paginated_articles = articles[start:end]
    total_pages = (total + size - 1) // size
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "articles": paginated_articles,
            "page": page,
            "size": size,
            "total": total,
            "total_pages": total_pages,
        }
    )


@router.get("/admin/articles/add", response_class=HTMLResponse, dependencies=[Depends(admin_auth)])
def add_article_page(request: Request):
    return templates.TemplateResponse("add_article.html", {"request": request})


@router.post("/admin/articles", dependencies=[Depends(admin_auth)])
def add_article_handler(title: str = Form(...), content: str = Form(...)):
    add_article(title, content)
    return RedirectResponse(url="/admin/articles", status_code=303)


@router.get("/admin/articles/{article_id}/edit", response_class=HTMLResponse, dependencies=[Depends(admin_auth)])
def edit_article_page(request: Request, article_id: str):
    article = get_article_by_id(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return templates.TemplateResponse("edit_article.html", {"request": request, "article": article})


@router.post("/admin/articles/{article_id}/edit", dependencies=[Depends(admin_auth)])
def edit_article_handler(article_id: str, title: str = Form(...), content: str = Form(...)):
    update_article(article_id, title, content)
    return RedirectResponse(url="/admin/articles", status_code=303)


@router.post("/admin/articles/{article_id}/delete", dependencies=[Depends(admin_auth)])
def delete_article_handler(article_id: str):
    delete_article(article_id)
    return RedirectResponse(url="/admin/articles", status_code=303)


@router.get("/admin/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "password_set": is_password_set()})


@router.post("/admin/login")
def login(request: Request, password: str = Form(...)):
    if not is_password_set():
        # Set new password
        if not password:
            return RedirectResponse(url="/admin/login", status_code=303)
        set_password(password)
        response = RedirectResponse(url="/admin/articles", status_code=303)
        response.set_cookie(key="admin_key", value="secret")
        return response
    # Validate password
    if validate_password(password):
        response = RedirectResponse(url="/admin/articles", status_code=303)
        response.set_cookie(key="admin_key", value="secret")
        return response
    return RedirectResponse(url="/admin/login", status_code=303)


@router.get("/admin/logout")
def logout():
    response = RedirectResponse(url="/admin/login", status_code=303)
    response.delete_cookie("admin_key")
    return response
