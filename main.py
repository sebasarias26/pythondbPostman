from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.modelosAPP import Usuario, Gasto, Categoria, MetodoPago, Base
from app.api.routes.rutas import rutas
from starlette.responses import RedirectResponse

#Activar el ORM que es un traductor entre python y omysql
Base.metadata.create_all(bind=engine) #Engine es la variable que contiene los datos de la bd

#variable para administrar la aplicación
app=FastAPI()

#Activo el api
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)