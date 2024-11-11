from fastapi import FastAPI

from utils.logUtil import log, console_logging_config
from usuarios import usuarios

app = FastAPI()

def init_application():
    console_logging_config()

    log.info("Starting application!")
  
@app.on_event("startup")
async def init_app():
    init_application()

@app.get("/")
def get_health_check():
    return {"Welcome!"}

@app.get("/health")
def get_health_check():
    return {"OK"}

app.include_router(usuarios.router, prefix="/usuarios")