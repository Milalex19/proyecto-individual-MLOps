![Logo](https://blog.soyhenry.com/content/images/2021/02/HEADER-BLOG-NEGRO-01.jpg)


# DATA SCIENCE - PROYECTO INDIVIDUAL
# Machine Learning Operations (MLOps)


# Proyecto de Predicción de Precios de Videojuegos en Steam

¡Bienvenido al proyecto de Predicción de Precios de Videojuegos en Steam! En este documento, te guiaré a través de los pasos esenciales que hemos seguido para abordar este emocionante desafío. Desde el análisis exploratorio de los datos hasta la implementación de una API para acceder a las predicciones del modelo, hemos creado una solución completa que proporciona información valiosa sobre los precios de los videojuegos en Steam.


![Logo](https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png)


## Descripción del Problema y Contexto

En el contexto actual, la plataforma de juegos Steam ha experimentado un crecimiento significativo, con una amplia gama de juegos disponibles en su plataforma. Sin embargo, la variabilidad en los precios de estos juegos puede ser un desafío tanto para los desarrolladores como para los jugadores. Por lo tanto, se ha propuesto este proyecto para abordar este problema y brindar una solución basada en datos.


## Pasos Clave del Proyecto:

### Datos

Se realizo la extracción de datos de un [dataset](https://github.com/Milalex19/proyecto-individual-MLOps/main/steam_game.json) el mismo se componen de 32135 filas (cada fila contiene un video juego) y 16 columnas (con atributos de cada titulo). 



## Transformación de Datos

Comenzamos por transformar los datos en un formato adecuado para el análisis. Aunque para el MVP no solicitan transformaciones complejas, he asegurado que los datos se lean correctamente y estén listos para su procesamiento.

- Los valores nulos de la columna release_date, se eliminaron del datset.

- Los valores nulos de la columna metascore, se rellenaron con el número 0.

- Los valores nulos de la columna sentiemnt, se rellenaron con Sin comentarios.

- se eliminaron columnas que no serián utilizadas, publisher, url, discount_price, reviews_url, app_name, tags, developer, id.

Se pueden visualizar las transformaciones y los análisis realizados en el siguiente [archivo](https://github.com/Milalex19/proyecto-individual-MLOps/main/ETL.ipynb)



## Análisis Exploratorio de Datos (EDA)

Realize un análisis exploratorio de los datos para comprender las relaciones entre las variables y detectar patrones interesantes. Mediante la visualización manual y la exploración de los datos, dentro de los análisis efectuados no se encuentraron correlaciones fuertes de las variables numéricas y se identificación de variables categóricas y sus valores.

Se efectuaron algunas transformaciones adicionales diferentes a las realizadas para la sección de ETL.

Se pueden visualizar las transformaciones y los análisis realizados en el siguiente
[archivo](https://github.com/Milalex19/proyecto-individual-MLOps/main/EDA.ipynb)



## Modelo de Predicción
Desarrolle un modelo de **`Machine Learning`** de regresion lineal que utiliza características como el género, metascore y sentiment para predecir los precios de los videojuegos.

Se define un preprocesador que escala las características numéricas y codifica las categóricas.

La función prediction toma el modelo entrenado (trained_model) y los valores de entrada (genero, metascore, sentiment) para realizar una predicción de precio y la raíz del error cuadrático medio (RMSE).

pueden visualizar los códigos realizados en el siguiente
[archivo](https://github.com/Milalex19/proyecto-individual-MLOps/main/modelo_MLOps.py)




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

[API](https://github.com/Milalex19/proyecto-individual-MLOps/blob/main/API.png)

## Deployment

Para el deploy de la API, se utilizó la plataforma **`Render`**.
Los datos están listos para ser consumidos y consultados a partir del siguiente link

[Link al Deployment](https://deploy-proyecto1.onrender.com/docs#/)



## Tecnologia usada
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
- Pikle


## Video 
Para consultar sobre los pasos del proceso y una explicación es posible acceder al siguiente [enlace]()
