from fastapi import FastAPI
from .routers import guest, admin

app = FastAPI()

app.include_router(guest.router)
app.include_router(admin.router)
