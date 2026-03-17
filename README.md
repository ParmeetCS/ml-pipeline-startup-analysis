# End to End Machine Learning Project 

## Project Architecture

```mermaid
graph TD
    A[Input Data] -->|Data Ingestion| B[Raw Data]
    B -->|Data Transformation| C[Processed Data]
    C -->|Train/Test Split| D{Data Split}
    D -->|Training Data| E[Model Trainer]
    D -->|Test Data| F[Model Evaluation]
    E -->|Trained Model| G[Model Storage]
    F -->|Performance Metrics| G
    G -->|Saved Model| H[Prediction Pipeline]
    I[User Input] -->|Flask Web App| H
    H -->|Prediction| J[Output Result]
    
    K[EDA Notebook] -.->|Data Analysis| C
    L[Model Training Notebook] -.->|Experiment| E
    
    style A fill:#e1f5ff
    style B fill:#e1f5ff
    style C fill:#e1f5ff
    style E fill:#fff3e0
    style G fill:#f3e5f5
    style H fill:#e8f5e9
    style J fill:#e8f5e9
```

## Project Structure

```
ml-pipeline-startup-analysis/
│
├── src/                          # Main source code
│   ├── components/               # Core ML components
│   │   ├── data_ingestion.py    # Data input handling
│   │   ├── data_transformation.py# Data preprocessing & feature engineering
│   │   └── model_trainer.py     # Model training logic
│   ├── pipelines/               # ML workflow pipelines
│   │   ├── train_pipeline.py    # Training pipeline
│   │   └── predict_pipeline.py  # Inference pipeline
│   ├── logger.py                # Logging utilities
│   ├── exception.py             # Custom exceptions
│   └── utils.py                 # Helper functions
│
├── notebook/                     # Jupyter notebooks
│   ├── EDA.ipynb                # Exploratory Data Analysis
│   └── Model Training.ipynb     # Model experimentation
│
├── templates/                    # Flask HTML templates
│   ├── home.html
│   └── index.html
│
├── app.py                        # Flask web application
├── setup.py                      # Package setup
├── requirements.txt              # Project dependencies
└── README.md                     # This file
```

## Workflow

1. **Data Ingestion** → Load and validate raw data
2. **Data Transformation** → Clean, preprocess, and engineer features
3. **Model Training** → Train ML models (CatBoost, XGBoost, Scikit-learn)
4. **Model Evaluation** → Validate model performance
5. **Prediction Pipeline** → Deploy model for inference
6. **Flask Web App** → User-friendly interface for predictions

## Technology Stack

- **Data Processing**: pandas, numpy
- **Visualization**: seaborn, matplotlib
- **Machine Learning**: scikit-learn, CatBoost, XGBoost
- **Web Framework**: Flask
- **Serialization**: dill