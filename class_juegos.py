import pandas as pd

# creo la clase video juego con todas las funciones solicitadas 
class Videojuegos:
    def __init__(self, data):
        self.data = data


    def existe_anio(self, anio):
        # Obtenemos todos los años únicos presentes en la columna 'release_date'
        anos_unicos = self.data['release_date'].dt.year.unique()
        # Verificamos si el año proporcionado está presente en la lista de años únicos
        return int(anio) in anos_unicos
           
    def genero(self, anio):
        anio_dt = pd.to_datetime(anio)
        # Se filtran los datos por el año ingresado
        df_anio_especifico = self.data[self.data['release_date'].dt.year == anio_dt.year]
        # se explorar la columna 'genres' para obtener los géneros únicos
        generos_unicos = df_anio_especifico['genres'].explode().unique()
        # Se inicia un diccionario para almacenar la cantidad de cada género
        ventas_por_genero = {}        
        # Se calcula la cantidad de cada género y se almacenan en el diccionario
        for genero in generos_unicos:
            ventas_por_genero[genero] = df_anio_especifico[df_anio_especifico['genres'].apply(lambda x: genero in x)]['title'].count()
        # Se ordena el diccionario según la cantidad en orden descendente
        generos_ordenados = dict(sorted(ventas_por_genero.items(), key=lambda x: x[1], reverse=True))
        # Se retornan los 5 primeros géneros con mayor cantidad
        generos_mas_vendidos = list(generos_ordenados.keys())[:5]
        return generos_mas_vendidos
    
      
    def juegos(self, anio):
        anio_dt = pd.to_datetime(anio)
        # Se filtran los datos por el año 
        df_anio_especifico = self.data[self.data['release_date'].dt.year == anio_dt.year]
        # Se obtiene la lista de juegos del año especificado
        juegos_anio = df_anio_especifico['title'].tolist()
        return juegos_anio    
        
    def specs(self, anio):
        anio_dt = pd.to_datetime(anio)
        # Se filtran los datos por el año 
        df_anio_especifico = self.data[self.data['release_date'].dt.year == anio_dt.year]
        # Se realiza el conteo de los specs y se toman los 5 que mas se repiten
        specs_counts = df_anio_especifico['specs'].explode().value_counts().nlargest(5)
        return specs_counts.index.tolist()

    def earlyacces(self, anio):
        anio_dt = pd.to_datetime(anio)
        # Se filtran los datos por el año y por early_access donde su condicion sea True
        df_anio_especifico = self.data[(self.data['release_date'].dt.year == anio_dt.year) & (self.data['early_access'] == True)]
        # Se realiza el conteo de los juecon con early_access
        juegos_con_early_access = len(df_anio_especifico)
        return juegos_con_early_access

    def sentiment(self, anio):
        anio_dt = pd.to_datetime(anio)
        # Se filtran los datos por el año
        df_anio_especifico = self.data[self.data['release_date'].dt.year == anio_dt.year]
        # Se calcula el recuento de valores únicos en la columna 'sentiment' de los datos y se devuelve un diccionario 
        sentiment_counts = df_anio_especifico['sentiment'].value_counts().to_dict()
        # Formateo el resultado en una cadena de texto para que retorne los valores en el formato solicitado
        formatted_result = "{ " + ", ".join([f"{key} = {value}" for key, value in sentiment_counts.items()]) + " }"
        return formatted_result
    
    def metascore(self, anio):
        anio_dt = pd.to_datetime(anio)
        # Se filtran los datos por el año
        df_anio_especifico = self.data[self.data['release_date'].dt.year == anio_dt.year]
        # Creo una condicional para verificar los valores de la columna metascore que sean iguales a cero para retornar un mensaje especifico
        if df_anio_especifico['metascore'].eq(0).all():
            return "No se encontro metascore para los juegos del año solicitado"
        # Si no hay datos en cero se continua con la ejecucion del codigo
        df_anio_especifico.loc[:, 'metascore'] 
        # Se ordenan el metascore por orden descendente
        df_ordenado = df_anio_especifico.sort_values(by='metascore', ascending=False)
        # filtramos los 5 juengos con mayor metascore y los retornamos
        top_5_juegos = df_ordenado[['title']].head(5)
        return top_5_juegos.to_dict(orient='records')