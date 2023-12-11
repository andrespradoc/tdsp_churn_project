##Ejemplo de implementación de modelo en producción

"""

Recuerde tener levantado el servicio del API del modelo con:

mlflow models serve -m 'models:/{model_name}/Production' -p {port} --env-manager 'local' &

"""

import requests
import time 
import json
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay, f1_score, recall_score, precision_score, accuracy_score

# Ejemplo de los valores que recibe la funcion de evaluacion
"""
data = [[3.601381662065445,
  -0.584935532922293,
  -1.5476529221334174,
  -0.7299871432508589,
  1.2558035395167784,
  -1.3007906138024043,
  0.31897761002330555,
  -0.3266240515743332,
  -0.4296567932454234,
  -1.8408912088049738,
  0.9256335994458792,
  0.6348485573724065],
 [0.18495105432263856,
  -0.584935532922293,
  -1.244013720966101,
  -0.1380816735819312,
  0.16508986969232622,
  -2.1947932578306815,
  1.8135194524172118,
  -0.3266240515743332,
  0.22417614376006004,
  0.4998636849042407,
  -0.35370363388816944,
  -0.1843703458003117]]
"""

"""
true_labels = [0,1]
"""

def get_labels_predicts(data: list):
    try: 
        init = time.time()
        r = requests.post("http://localhost:8124/invocations", json={"inputs": data})
        final = time.time()
        print(r.text, f'Tiempo de respuesta: {final-init}') ## por ejemplo retorna {"predictions": [0, 1]}  Tiempo de respuesta: 0.155
        return r.json()    
    except Exception as ex:
        print(ex)

def evaluation_model(data, true_labels):
  predicts = get_labels_predicts(data)
  f1_ev = f1_score(true_labels, predicts)
  acc_ev = accuracy_score(true_labels, predicts)
  precision_ev = precision_score(true_labels, predicts)
  recall_ev = recall_score(true_labels, predicts)
  print(f"accuracy: {acc_ev} \n precision: {precision_ev}\n recall: {recall_ev}\n f1_score: {f1_ev}")
  cm = confusion_matrix(true_labels, predicts)
  disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['no', 'yes'])
  disp.plot()
  
  if __name__ == '__main__':
      evaluation_model(data, 
                       true_labels)