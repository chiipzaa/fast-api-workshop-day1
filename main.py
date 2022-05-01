from fastapi import FastAPI

from models.database import engine
from models.inventory import inventory_model
from models.users import users_model

from routers.inventory import inventory_router
from routers.users import users_router
from routers.auth import authen_router

app = FastAPI(
    title="fastapi workshop x flutter 2020",
    description="",
    version="0.0.1",
    terms_of_service="https://www.teamramweb.com/terms/",
    contact={
        "name": "Teerasit Arttantra",
        "url": "https://www.teamramweb.com/contact/",
        "email": "info@teamtamweb.com",
    },
)
app.include_router(inventory_router.router)
app.include_router(users_router.router)
app.include_router(authen_router.router)


@app.get("/")
def hello():
    return {"Hello": "FastAPI"}


inventory_model.Base.metadata.create_all(engine)
users_model.Base.metadata.create_all(engine)
