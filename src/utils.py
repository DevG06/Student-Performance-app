import os
import sys
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as f:
            dill.dump(obj, f)
        logging.info(f'Object saved to {file_path}')
    
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]
            model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)
            r2_test = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = r2_test

        return report
    
    except Exception as e:
        CustomException(e, sys)