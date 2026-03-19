import os
import sys
from dataclasses import dataclass

from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingClassifier

from src.exception import CustomException
from src.logger import logging
from src.utils import evaluate_models,save_object


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Spliy training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models={
                "Logistic Regression": LogisticRegression(),
                "Decision Tree": DecisionTreeClassifier(),
                "Random Forest": RandomForestClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(),
                "XGBoost": XGBClassifier()
            }
            params={
                "Logistic Regression": {
        'C': [0.01, 0.1, 1, 10, 100],
            'solver': ['lbfgs']
    },

    "Decision Tree": {
        'criterion': ['gini', 'entropy', 'log_loss'],
        'max_depth': [None, 5, 10, 20],
        'min_samples_split': [2, 5, 10]
    },

    "Random Forest": {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 5, 10],
        'min_samples_split': [2, 5],
        'max_features': ['sqrt', 'log2']
    },

    "Gradient Boosting": {
        'learning_rate': [0.01, 0.05, 0.1],
        'n_estimators': [50, 100, 200],
        'subsample': [0.7, 0.8, 0.9]
    },

    "XGBoost": {
        'learning_rate': [0.01, 0.05, 0.1],
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 7]
    }
            }

            model_report:dict=evaluate_models(
                X_Train=X_train,
                Y_Train=y_train,
                X_Test=X_test,
                Y_Test=y_test,
                models=models,
                param=params
            )
            best_model_score=max(model_report.values())

            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model=models[best_model_name]
            if best_model_score<0.6:
                raise CustomException("No best model found",sys)
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            accuracy=accuracy_score(y_test,predicted)
            return accuracy
        except Exception as e:
            raise CustomException(e,sys)
            

            
