from fastapi import Request, HTTPException, status


def admin_auth(request: Request):
    api_key = request.cookies.get("admin_key")
    if api_key != "secret":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
