from fastapi import APIRouter, HTTPException
import pandas as pd
import joblib
from class_juegos import Videojuegos # Se importa la clase video juegos
from modelo_MLOps import prediction # Importa la función de predicción
from models import GeneroEnum, SentimentEnum
from fastapi.responses import JSONResponse

# Se carga el DataFrame desde un archivo CSV y seconvierte la columna 'release_date' al tipo de dato datetime
df = pd.read_csv("steam_games.csv", parse_dates=['release_date'])

# Se crea una instancia de la clase Videojuegos
analyzer = Videojuegos(df)

# Crea una instancia de FastAPI
router = APIRouter()

# se define una funcion para status code
def validar_formato_anio(year: str):
    if not year.isdigit() or len(year) != 4:
        raise HTTPException(status_code=400, detail="El formato del año es incorrecto. Debe ser un valor numérico de cuatro dígitos (YYYY).")
    if not analyzer.existe_anio(year):
        raise HTTPException(status_code=404, detail=f"El año {year} no se encuentra en los datos.")
  
# Se Definen las rutas y funciones para cada método de la clase Videojuegos
  
@router.get("/genero/{year}", description="Consulta el género más común de los videojuegos en el año solicitado.\nEl año debe estar en formato YYYY (cuatro dígitos numéricos).")
async def genero(year: str):
    validar_formato_anio(year)
    genero = analyzer.genero(year)
    return {"year": year, "genero": genero}

@router.get("/juegos/{year}", description="Consulta el nombre de los videojuegos mas nombrados en el año solicitado.\nEl año debe estar en formato YYYY (cuatro dígitos numéricos).")
async def juegos(year: str):
    validar_formato_anio(year)
    juegos = analyzer.juegos(year)
    return {"year": year, "juegos": juegos}

@router.get("/specs/{year}", description="Consulta el specs de los videojuegos mas comunes del año solicitado.\nEl año debe estar en formato YYYY (cuatro dígitos numéricos).")
async def specs(year: str):
    validar_formato_anio(year)
    specs = analyzer.specs(year)
    return {"year": year, "specs": specs}

@router.get("/earlyacces/{year}", description="Consulta los videojuegos con earlyacces para el año solicitado.\nEl año debe estar en formato YYYY (cuatro dígitos numéricos).")
async def earlyacces(year: str):
    validar_formato_anio(year)
    early_access = analyzer.earlyacces(year)
    return {"year": year, "earlyacces": early_access}

@router.get("/sentiment/{year}", description="Consulta la calificacion de sentimientos de los videojuegos para el año solicitado.\nEl año debe estar en formato YYYY (cuatro dígitos numéricos).")
async def sentimiento(year: str):
    validar_formato_anio(year)
    sentimiento = analyzer.sentiment(year)
    return {"year": year, "sentimiento": sentimiento}

@router.get("/metascore/{year}", description="Consulta los puntajes de los videojuegos para elaño solicitado.\nEl año debe estar en formato YYYY (cuatro dígitos numéricos).")
async def metascore(year: str):
    validar_formato_anio(year)
    metascore = analyzer.metascore(year)
    return {"year": year, "metascore": metascore}
     

@router.get("/predict/", description="Realiza una prediccion de precio de video juegos teniendo en cuenta el genero, el mesacore y el sentiment.")
def predict(genero: GeneroEnum, metascore: float, sentiment: SentimentEnum):
     # Cargar el rmse entrenado
    rmse_modelo = joblib.load('rmse_modelo.pkl')
    # Cargar el modelo entrenado
    trained_model = joblib.load('modelo_entrenado.pkl')
    # Crear un DataFrame con los valores de entrada para hacer la predicción
    data = pd.DataFrame({'genres': [genero], 'metascore': [metascore], 'sentiment': [sentiment]})
    # Realizar la predicción utilizando el modelo entrenado
    price_pred = trained_model.predict(data)
    # Crear un diccionario con las claves y los valores
    output_dict = {
        "predicted_price": round(price_pred[0], 2),
        "RMSE": round(rmse_modelo, 2)
    }
  
    # Devolver la respuesta como JSON
    return JSONResponse(content=output_dict) 