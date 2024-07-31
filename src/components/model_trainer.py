import os
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_training_config = ModelTrainerConfig()
    
    def initiate_model_training(self, train_arr, test_arr):
        try:
            logging.info("Entering the model training method")
            logging.info("Splitting training and testing data")
            X_train, y_train, X_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            models = {
                'Linear Regression': LinearRegression(),
                'Decision Tree': DecisionTreeRegressor(),
                'Random Forest': RandomForestRegressor(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'AdaBoost': AdaBoostRegressor(),
                'K-Nearest Neighbors': KNeighborsRegressor(),
                'XGBoost': XGBRegressor(),
                'CatBoost': CatBoostRegressor(verbose=False)
            }
            logging.info("Starting model training")

            model_report : dict = evaluate_model(X_train, y_train, X_test, y_test, models)

            logging.info("Model training completed")

            # Find best model score
            best_model_score = max(sorted(model_report.values()))

            # Find best model name
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            logging.info(f"Best model: {best_model_name} with score : {best_model_score}")

            if best_model_score < 0.6:
                raise CustomException("No best model found")
            
            best_model = models[best_model_name]

            logging.info("Saving model")
            save_object(
                file_path=self.model_training_config.trained_model_file_path,
                obj=best_model
            )
            logging.info("Model saved")

            predicted = best_model.predict(X_test)

            r2 = r2_score(y_test, predicted)
            return r2

        except Exception as e:
            CustomException(e, sys)
