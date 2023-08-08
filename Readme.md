![Logo](https://blog.soyhenry.com/content/images/2021/02/HEADER-BLOG-NEGRO-01.jpg)


# DATA SCIENCE - PROYECTO INDIVIDUAL
# Machine Learning Operations (MLOps)


# Proyecto de Predicción de Precios de Videojuegos en Steam - Documento README
¡Bienvenido al proyecto de Predicción de Precios de Videojuegos en Steam! En este documento, te guiaré a través de los pasos esenciales que hemos seguido para abordar este emocionante desafío. Desde el análisis exploratorio de los datos hasta la implementación de una API para acceder a las predicciones del modelo, hemos creado una solución completa que proporciona información valiosa sobre los precios de los videojuegos en Steam.


![Logo](https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png)


## Descripción del Problema y Contexto
Tienes tu modelo de recomendación dando unas buenas métricas 😏, y ahora, cómo lo llevas al mundo real? 👀

El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.


El [dataset](https://github.com/Milalex19/proyecto-individual-MLOps/blob/main/steam_game.json) contiene información acerca viedo juegos. El mismo cuenta con 32135 filas (cada fila contiene un video juego) y 16 columnas (con atributos de cada título).

## Transformación de Datos

Comenzamos por transformar los datos en un formato adecuado para el análisis. Aunque para el MVP no solicitan transformaciones complejas, he asegurado que los datos se lean correctamente y estén listos para su procesamiento.

- Los valores nulos de la columna release_date, se eliminaron del datset.

- Los valores nulos de la columna metascore, se rellenaron con el número 0.

- Los valores nulos de la columna sentiemnt, se rellenaron con Sin comentarios.

- se eliminaron columnas que no serián utilizadas, publisher, url, discount_price, reviews_url, app_name, tags, developer, id.

Se pueden visualizar las transformaciones y los análisis realizados en el siguiente [archivo](https://github.com/Milalex19/proyecto-individual-MLOps/blob/main/ETL.ipynb)


## Desarrollo de la API

Cree una API a través del Framework **`FastAPI`** que ofrece una variedad de consultas útiles relacionadas con los videojuegos. He desarrollado funciones para obtener in fomacion como: 

def genero( Año: str ): Se ingresa un año y devuelve los 5 géneros más repetidos en orden.

def juegos( Año: str ): Se ingresa un año y devuelve los juegos encontados en el año.

def specs( Año: str ): Se ingresa un año y devuelve los 5 specs que más se repiten en orden.

def earlyacces( Año: str ): Se ingresa un año y devuelve los juegos early access.

def sentiment( Año: str ): Se ingresa un año y devuelve la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.

                    Ejemplo de retorno: {Mixed = 182, Very Positive = 120, Positive = 278}

def metascore( Año: str ): Se ingresa un año y devuelve los 5 juegos con mayor metascore.

Estos endpoints se han diseñado para proporcionar información a los usuarios y permitir un acceso fácil a través de solicitudes HTTP.

El código para correr la API dentro de FastAPI se puede visualizar [aquí](https://github.com/Milalex19/proyecto-individual-MLOps/blob/main/consultas.py) 


## Análisis Exploratorio de Datos (EDA)

Realizamos un análisis exploratorio de los datos para comprender las relaciones entre las variables y detectar patrones interesantes. Mediante la visualización manual y la exploración de los datos, dentro de los análisis efectuados no se encuentraron correlaciones fuertes de las variables numéricas y se identificación de variables categóricas y sus valores.

Se efectuaron algunas transformaciones adicionales diferentes a las realizadas para la sección de ETL.

Se pueden visualizar las transformaciones y los análisis realizados en el siguiente
[archivo](https://github.com/Milalex19/proyecto-individual-MLOps/blob/main/EDA.ipynb)


## Modelo de Predicción
Desarrolle un modelo de **`Machine Learning`** de regresion lineal que utiliza características como el género, metascore y sentiment para predecir los precios de los videojuegos.

Se define un preprocesador que escala las características numéricas y codifica las categóricas.

La función prediction toma el modelo entrenado (trained_model) y los valores de entrada (genero, metascore, sentiment) para realizar una predicción de precio y la raíz del error cuadrático medio (RMSE).

e pueden visualizar los códigos realizados en el siguiente
[archivo](https://github.com/Milalex19/proyecto-individual-MLOps/blob/main/modelo_MLOps.py)



## Deployment

Para el deploy de la API, se utilizó la plataforma **`Render`**.
Los datos están listos para ser consumidos y consultados a partir del siguiente link

[Link al Deployment](https://deploy-proyecto-1-henry.onrender.com/docs#/)



## Video 

Para consultar sobre los pasos del proceso y una explicación es posible acceder al siguiente [enlace](https://www.youtube.com/watch?v=7rNNCXf-Bh4)