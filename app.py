from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import time

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/favicon", response_class=HTMLResponse)
async def favicon(request: Request):
    return templates.TemplateResponse("favicon.html", {"request": request})

@app.get("/rules", response_class=HTMLResponse)
async def rules(request: Request):
    return templates.TemplateResponse("rules.html", {"request": request})
