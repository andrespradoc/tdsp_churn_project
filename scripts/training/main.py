import pandas as pd
import os
import numpy as np
import mlflow, optuna
from pyngrok import ngrok
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, recall_score, precision_score

#Levantar servidor MLFlow

"""
command_mlflow_start_server = "mlflow server \ --backend-store-uri sqlite:///tracking.db \ --default-artifact-root file:mlruns \ -p 5000 &"

get_ipython().system_raw(command_mlflow_start_server)
mlflow.set_tracking_uri("http://localhost:5000")

"""

#Conectarse a MLFlow por medio de NGROK
token = "xxxxxxxxxxxxxxxxxx" # Agregue el token dentro de las comillas
os.environ["NGROK_TOKEN"] = token
ngrok.connect(5000, "http")


#Leer datos preprocesados

X_test = pd.read_csv('X_test.csv', sep = ';').to_numpy()
y_test = pd.read_csv('y_test.csv', sep = ';').to_numpy()
X_train = pd.read_csv('X_train.csv', sep = ';').to_numpy()
y_train = pd.read_csv('y_train.csv', sep = ';').to_numpy()

#Definir experimento de ML_FLow
exp_name = 'random_forest_classifier'
exp = mlflow.create_experiment(name=exp_name, artifact_location="mlruns")

#Funcion Entrenar modelo con hiperparametros default
def default_rfc_model(X_train, y_train, X_test, y_test):
  model = RandomForestClassifier()
  model = model.fit(X_train, y_train)
  y_predict = model.predict(X_test)
  metrics = {
      'f1_score': f1_score(y_pred=y_predict, y_true=y_test),
      'recall':recall_score(y_pred=y_predict, y_true=y_test),
      'precision':precision_score(y_pred=y_predict, y_true=y_test)
  }
  return model, metrics

#Funcion entrenar modelo ajustando hiperparametros
def config_rfc_model(X_train, y_train, X_test, y_test, n_estimators, criterion, max_depth, max_features, random_state, class_weight):
  model = RandomForestClassifier(n_estimators=n_estimators, criterion = criterion, max_depth=max_depth, 
                                 max_features=max_features, random_state= random_state, class_weight=class_weight)
  model = model.fit(X_train, y_train)
  y_predict = model.predict(X_test)
  metrics = {
      'f1_score': f1_score(y_pred=y_predict, y_true=y_test),
      'recall':recall_score(y_pred=y_predict, y_true=y_test),
      'precision':precision_score(y_pred=y_predict, y_true=y_test)
  }
  return model, metrics

#Funcion para registrar modelo por defecto en MLFlow
def mlflow_run_logs(X_train, y_train, X_test, y_test, run_name, exp_id):
  with mlflow.start_run(
      run_name = run_name,
      experiment_id=exp_id
  ) as mlflow_run:
    model, metrics = default_rfc_model(X_train, y_train, X_test, y_test)
    mlflow.sklearn.log_model(model, 'rfc_default')
    mlflow.log_metrics(metrics)
    mlflow.log_params(model.get_params())
    mlflow.end_run()
    return mlflow_run, model, metrics

# Funcion para registrar modelo ajustando hiperparametros en MLFlow

def mlflow_run_logs_tune(X_train, y_train, X_test, y_test, n_estimators, criterion, max_depth, max_features, random_state, class_weight,run_name, exp_id):
  with mlflow.start_run(
      run_name = run_name,
      experiment_id=exp_id
  ) as mlflow_run:
    model, metrics = config_rfc_model(X_train, y_train, X_test, y_test, n_estimators, criterion, max_depth, max_features, random_state, class_weight)
    mlflow.sklearn.log_model(model, 'rfc_tune')
    mlflow.log_metrics(metrics)
    mlflow.log_params(model.get_params())
    mlflow.end_run()
    return mlflow_run, model, metrics

# Generar busqueda de hiperparametros con optuna

def objective(trial):
    ###
    n_estimators=trial.suggest_int('n_estimators',100,500,50)
    criterion = trial.suggest_categorical('criterion',['gini', 'entropy', 'log_loss'])
    max_depth=trial.suggest_int('max_depth', 20, 100,5)
    max_features=trial.suggest_categorical('max_features', ['sqrt', 'log2']) 
    random_state = 1 
    class_weight=trial.suggest_categorical('class_weight', ['balanced', 'balanced_subsample'])
    run_name = 'optuna_2'
    exp_id = exp
    mlflow_run, model, metrics = mlflow_run_logs_tune(X_train, y_train, X_test, y_test, n_estimators, criterion, max_depth, max_features, random_state, class_weight,run_name, exp_id)
    return metrics['f1_score']

def run_experiments():
    #Ejecutar experimento con los hiperparametros default
    run_stat, model, metrics = mlflow_run_logs(X_train, y_train, X_test, y_test, 'rfc_default_params', exp)
    #Ejecutar experimento variando hiperparametros con Optuna
    study = optuna.create_study(
    direction="maximize",
    storage="sqlite:///hp.db",
    study_name="rfc_tunning",
    load_if_exists = True
    )
    study.optimize(func=objective, n_trials=50, n_jobs=1)
    best_params = study.best_params
    best_paramsscore = study.best_value
    return best_params, best_score

if __name__ == '__main__'
    run_experiments()