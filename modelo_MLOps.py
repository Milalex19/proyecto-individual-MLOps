import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib

df = pd.read_csv('game_modelo.csv')

def train_model(df):
  
    # Se dividen los datos en características (X) y etiquetas (y)
    X = df[['genres', 'metascore', 'sentiment']]
    y = df['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # Se define el preprocesamiento de las características
    categorical_features = ['genres', 'sentiment']
    numeric_features = ['metascore']
    numeric_transformer = Pipeline(steps=[('scaler', MinMaxScaler())])
    categorical_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])
    preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, numeric_features),
                                                   ('cat', categorical_transformer, categorical_features)])
    
    # Crear el modelo de regresión lineal
    model = LinearRegression()
    
    # Crear el pipeline que combina el preprocesamiento y el modelo
    pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('regressor', model)])
    
    # Entrenar el modelo
    pipeline.fit(X_train, y_train)
    
    # Calcular el error cuadrático medio (RMSE) en el conjunto de prueba
    y_pred = pipeline.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
 
    return pipeline, rmse

def prediction(trained_model, genero, metascore, sentiment):

    # Realizar predicciones en el conjunto de prueba
    data = pd.DataFrame({'genres': [genero], 'metascore': [metascore], 'sentiment': [sentiment]})

    # Realizar la predicción utilizando el modelo entrenado
    price_pred = trained_model.predict(data)

    return price_pred[0]