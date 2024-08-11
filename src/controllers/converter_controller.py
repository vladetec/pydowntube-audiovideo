from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse

from src.models.converter import download_video
from src.views.converter import render_template

converter = APIRouter()


@converter.get("/", response_class=HTMLResponse)
async def get_form():
    return render_template("converter.html")


@converter.post("/convert", response_class=HTMLResponse)
async def convert_video(
    request: Request, url: str = Form(...), format: str = Form(...)
):
    file_name = download_video(url, format)
    return render_template("converter.html", {"file_name": file_name})
