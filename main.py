from fastapi import FastAPI
from router import consultas

 
# Crea una instancia de FastAPI
app = FastAPI(title = "Proyecto induvidual MLOps - Miller Rodiguez", descripcion = "API para consulta y prediccion de precios de video juegos")


app.include_router(consultas.router)



@app.get("/")
async def root():
    return "Bienvenidos A lA API"