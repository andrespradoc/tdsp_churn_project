import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def preprocessing_data():
    #Leer dataset

    df_dataset = pd.read_csv('src/database/telecom-customer-churn.zip', compression='zip')

    ### Datos categoricos texto a binario

    for column in ['Churn', 'Intl_Plan', 'Vmail_Plan']:
            df_dataset[column] = df_dataset[column].replace({'no':0 , 'yes':1})

    ### Eliminar variables fuertemente correlacionadas que pueden afectar la prediccion del modelo

    df_filter = df_dataset.drop(columns =['Vmail_Plan', 'Day_Charge', 'Eve_Charge', 'Night_Charge', 'Intl_Charge'])

    ####Eliminar columnas que son identificadores unicos de cada registro, por lo tanto no son suficientes para discriminar los registros
    df_filter = df_filter.drop(columns=['Area_Code', 'State', 'Phone'])

    #### Nueva matriz de correlación
    plt.figure(figsize = (16, 16))
    heatmap  = sns.heatmap(df_filter.corr(),vmin=-1, vmax=1, annot=True)
    heatmap.set_title('Correlation Matrix')

    ### Obtener variables exogenas y endogena

    X = df_filter.drop(columns='Churn')
    y = df_filter['Churn']

    ### Particion de datos de entrenamiento y pruebas

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 30)

    ### Visualizar el problema de escalas entre datos

    print(X_test.describe())

    ### Debido a que los registros manejan diferentes magnitudes 
    ###y diferentes rangos, se hace un escalamiento a los datos de entrenamiento y prueba

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    print(X_train)
    X_test = scaler.fit_transform(X_test)
    print(X_test)

    ### Visualización estadistica de la data reescalada

    X_test_df = pd.DataFrame(columns = X.columns, data=X_test)
    X_test_df.describe()

    return X_train, X_test, y_train, y_test


if __name__ == '__main__':
    preprocessing_data()