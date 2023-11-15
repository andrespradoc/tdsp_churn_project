import requests
import pandas as pd
import zipfile
import io
import os
from kaggle.api.kaggle_api_extended import KaggleApi

### Descargar dataset de kaggle mediante la API

api = KaggleApi()
api.authenticate()
api.dataset_download_files('nushkaa/telecom-customer-churn', path="src/database")

### Leer dataset con pandas
df_dataset = pd.read_csv('src/database/telecom-customer-churn.zip', compression='zip')

### Imprimir un resumen estadistico de los campos del dataset
print(df_dataset.describe())

'''
Account_Length	Vmail_Message	Day_Mins	Eve_Mins	Night_Mins	Intl_Mins	CustServ_Calls	Day_Calls	Day_Charge	Eve_Calls	Eve_Charge	Night_Calls	Night_Charge	Intl_Calls	Intl_Charge	Area_Code
count	3333.000000	3333.000000	3333.000000	3333.000000	3333.000000	3333.000000	3333.000000	3333.000000	3333.000000	3333.000000	3333.000000	3333.000000	3333.000000	3333.000000	3333.000000	3333.000000
mean	101.064806	8.099010	179.775098	200.980348	200.872037	10.237294	1.562856	100.435644	30.562307	100.114311	17.083540	100.107711	9.039325	4.479448	2.764581	437.182418
std	39.822106	13.688365	54.467389	50.713844	50.573847	2.791840	1.315491	20.069084	9.259435	19.922625	4.310668	19.568609	2.275873	2.461214	0.753773	42.371290
min	1.000000	0.000000	0.000000	0.000000	23.200000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	33.000000	1.040000	0.000000	0.000000	408.000000
25%	74.000000	0.000000	143.700000	166.600000	167.000000	8.500000	1.000000	87.000000	24.430000	87.000000	14.160000	87.000000	7.520000	3.000000	2.300000	408.000000
50%	101.000000	0.000000	179.400000	201.400000	201.200000	10.300000	1.000000	101.000000	30.500000	100.000000	17.120000	100.000000	9.050000	4.000000	2.780000	415.000000
75%	127.000000	20.000000	216.400000	235.300000	235.300000	12.100000	2.000000	114.000000	36.790000	114.000000	20.000000	113.000000	10.590000	6.000000	3.270000	510.000000
max	243.000000	51.000000	350.800000	363.700000	395.000000	20.000000	9.000000	165.000000	59.640000	170.000000	30.910000	175.000000	17.770000	20.000000	5.400000	510.000000
'''

### Visualizar si hay datos faltantes
print(df_dataset.isna().sum())
'''
Account_Length    0
Vmail_Message     0
Day_Mins          0
Eve_Mins          0
Night_Mins        0
Intl_Mins         0
CustServ_Calls    0
Churn             0
Intl_Plan         0
Vmail_Plan        0
Day_Calls         0
Day_Charge        0
Eve_Calls         0
Eve_Charge        0
Night_Calls       0
Night_Charge      0
Intl_Calls        0
Intl_Charge       0
State             0
Area_Code         0
Phone             0
dtype: int64
''' 

### Ver el tipo de datos de las columnas
print(df_dataset.info())
'''
RangeIndex: 3333 entries, 0 to 3332
Data columns (total 21 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   Account_Length  3333 non-null   int64  
 1   Vmail_Message   3333 non-null   int64  
 2   Day_Mins        3333 non-null   float64
 3   Eve_Mins        3333 non-null   float64
 4   Night_Mins      3333 non-null   float64
 5   Intl_Mins       3333 non-null   float64
 6   CustServ_Calls  3333 non-null   int64  
 7   Churn           3333 non-null   object 
 8   Intl_Plan       3333 non-null   object 
 9   Vmail_Plan      3333 non-null   object 
 10  Day_Calls       3333 non-null   int64  
 11  Day_Charge      3333 non-null   float64
 12  Eve_Calls       3333 non-null   int64  
 13  Eve_Charge      3333 non-null   float64
 14  Night_Calls     3333 non-null   int64  
 15  Night_Charge    3333 non-null   float64
 16  Intl_Calls      3333 non-null   int64  
 17  Intl_Charge     3333 non-null   float64
 18  State           3333 non-null   object 
 19  Area_Code       3333 non-null   int64  
 20  Phone           3333 non-null   object 
dtypes: float64(8), int64(8), object(5)
memory usage: 546.9+ KB
'''

### Distribución de las etiquetas a predecir 
print(df_dataset['Churn'].value_counts())
'''
no     2850
yes     483
Name: Churn, dtype: int64
'''

### Variable endogena categórica tipo texto a binario (0-1)

y = df_dataset['Churn'].replace({'no': 0, 'yes': 1}).to_numpy()
a = np.bincount(y)
ii = np.nonzero(a)[0]
out = np.vstack((ii, a[ii])).T
print(out)

'''
[[   0 2850]
 [   1  483]]
'''
