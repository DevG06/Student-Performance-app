import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

def training_pipeline():
    try:
        # Step 1: Data Ingestion
        logging.info("Starting data ingestion")
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        
        # Step 2: Data Transformation
        logging.info("Starting data transformation")
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_obj_path = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        
        # Step 3: Model Training
        logging.info("Starting model training")
        model_trainer = ModelTrainer()
        model_performance = model_trainer.initiate_model_training(train_arr, test_arr)
        
        logging.info(f"Model training completed. Best model performance: {model_performance}")

    except Exception as e:
        logging.error(f"Error in training pipeline: {str(e)}")
        raise CustomException(e, sys)

if __name__ == "__main__":
    training_pipeline()
