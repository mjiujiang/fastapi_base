import uvicorn
from fastapi import FastAPI

from app import api_user

from app.database import models
from app.database.database import engine

models.Base.metadata.create_all(bind=engine)


def create_app():
    fast_app = FastAPI(debug=True)
    fast_app.include_router(api_user.router)

    return fast_app


app = create_app()









if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, debug=True, reload=True, lifespan='on')
