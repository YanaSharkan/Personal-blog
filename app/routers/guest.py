from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ..services.articles_services import get_articles, get_article_by_id

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def home(
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
        "home.html",
        {
            "request": request,
            "articles": paginated_articles,
            "page": page,
            "size": size,
            "total": total,
            "total_pages": total_pages,
        }
    )


@router.get("/articles/{article_id}", response_class=HTMLResponse)
def article_page(request: Request, article_id: str):
    article = get_article_by_id(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return templates.TemplateResponse("article.html", {"request": request, "article": article})
