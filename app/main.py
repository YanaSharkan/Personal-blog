import os
import json
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .routers import guest, admin


app = FastAPI()

app.include_router(guest.router)
app.include_router(admin.router)


@app.on_event("startup")
def ensure_admin_json():
    core_dir = os.path.join(os.path.dirname(__file__), 'core')
    admin_path = os.path.join(core_dir, 'admin.json')
    os.makedirs(core_dir, exist_ok=True)
    if not os.path.exists(admin_path):
        with open(admin_path, 'w', encoding='utf-8') as f:
            json.dump({"password_hash": ""}, f, ensure_ascii=False, indent=2)


# Mount static directory
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")


@app.get("/favicon.ico")
def favicon():
    return FileResponse(os.path.join(os.path.dirname(__file__), "static", "favicon.ico"))
