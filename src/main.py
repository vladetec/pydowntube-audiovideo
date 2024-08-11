from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .controllers.converter_controller import converter

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")

app.include_router(converter)
