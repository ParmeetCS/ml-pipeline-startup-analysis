import sys

from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainPipeline:
	def __init__(self):
		self.data_ingestion = DataIngestion()
		self.data_transformation = DataTransformation()
		self.model_trainer = ModelTrainer()

	def run_pipeline(self):
		try:
			logging.info("Training pipeline started")

			train_data_path, test_data_path = self.data_ingestion.initiate_data_ingestion()

			train_arr, test_arr, _ = self.data_transformation.intitiate_data_transformation(
				train_data_path,
				test_data_path,
			)

			model_score = self.model_trainer.initiate_model_trainer(train_arr, test_arr)
			logging.info("Training pipeline completed with accuracy: %s", model_score)

			return model_score
		except Exception as e:
			raise CustomException(e, sys)


if __name__ == "__main__":
	pipeline = TrainPipeline()
	print(pipeline.run_pipeline())
