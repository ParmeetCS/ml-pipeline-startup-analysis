import os
import sys

import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV
from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_Train,Y_Train,X_Test,Y_Test,models,param,use_search=False):
    try:
       report={}
       for model_name,model in models.items():
           para=param[model_name]
           if use_search:
               search = RandomizedSearchCV(
                   estimator=model,
                   param_distributions=para,
                   n_iter=5,
                   cv=2,
                   scoring='accuracy',
                   n_jobs=1,
                   random_state=42
               )
               search.fit(X_Train,Y_Train)
               model.set_params(**search.best_params_)
           model.fit(X_Train, Y_Train)
           y_train_pred = model.predict(X_Train)
           y_test_pred = model.predict(X_Test)
           train_model_score = accuracy_score(Y_Train, y_train_pred)
           test_model_score = accuracy_score(Y_Test, y_test_pred)
           print(f"{model_name}")
           print(f"Train Accuracy: {train_model_score:.4f}")
           print(f"Test Accuracy: {test_model_score:.4f}")
           print("="*35)
           
           report[model_name] = test_model_score
       return report

    except Exception as e:
        raise CustomException(e,sys)

def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)