import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def exploratory_data():
    # Leer datos de la DB almacenada en el repositorio
    df_dataset = pd.read_csv('src7database/telecom-customer-churn.zip', compression='zip')

    ### Media - Min - Max - Desviación standar - rangos intercuartiles
    print(df_dataset.describe())

    ### Registros Nulos
    print(df_dataset.isna().sum())

    ### Describir columnas a nivel de tipo de datos del dataset
    print(df_dataset.info())

    ### Cantidad de registros por etiqueta a predecir

    print(df_dataset['Churn'].value_counts())

    ### Cantidad de churn por Lineas con Plan de voz internacional

    print(df_dataset[['Intl_Plan', 'Churn', 'Phone']].groupby(by=['Intl_Plan','Churn']).count())

    ### Churn por Plan de Buzon de voz

    print(df_dataset[['Vmail_Plan', 'Churn', 'Phone']].groupby(by=['Vmail_Plan','Churn']).count())

    ### Convertir variables categoricas a valor binario

    for column in ['Churn', 'Intl_Plan', 'Vmail_Plan']:
        df_dataset[column] = df_dataset[column].replace({'no':0 , 'yes':1})

    ### Matriz de correlación

    plt.figure(figsize = (16, 16))
    heatmap  = sns.heatmap(df_dataset.corr(),vmin=-1, vmax=1, annot=True)
    heatmap.set_title('Correlation Matrix')

    ### Correlación de la variable objetivo con las demas variables

    plt.figure(figsize = (16, 16))
    heatmap  = sns.heatmap(df_dataset.corr()[['Churn']].sort_values(by='Churn', ascending=False),vmin=-1, vmax=1, annot=True)
    heatmap.set_title('Correlation Matrix with Churn variable')

if __name__ == '__main__':
    exploratory_data()