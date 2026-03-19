import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,feature):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')

            if not os.path.exists(model_path):
                raise FileNotFoundError("Trained model not found at artifacts/model.pkl. Run training pipeline first.")

            if not os.path.exists(preprocessor_path):
                raise FileNotFoundError("Preprocessor not found at artifacts/preprocessor.pkl. Run training pipeline first.")

            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(feature)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 funding_rounds: int,
                 founder_experience_years: int,
                 team_size: int,
                 market_size_billion: float,
                 product_traction_users: int,
                 burn_rate_million: float,
                 revenue_million: float,
                 investor_type: str,
                 sector: str,
                 founder_background: str):

        self.funding_rounds = funding_rounds
        self.founder_experience_years = founder_experience_years
        self.team_size = team_size
        self.market_size_billion = market_size_billion
        self.product_traction_users = product_traction_users
        self.burn_rate_million = burn_rate_million
        self.revenue_million = revenue_million
        self.investor_type = investor_type
        self.sector = sector
        self.founder_background = founder_background

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "funding_rounds": [self.funding_rounds],
                "founder_experience_years": [self.founder_experience_years],
                "team_size": [self.team_size],
                "market_size_billion": [self.market_size_billion],
                "product_traction_users": [self.product_traction_users],
                "burn_rate_million": [self.burn_rate_million],
                "revenue_million": [self.revenue_million],
                "investor_type": [self.investor_type],
                "sector": [self.sector],
                "founder_background": [self.founder_background],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)