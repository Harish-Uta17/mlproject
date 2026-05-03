# Student Exam Performance Predictor

An end-to-end machine learning project that predicts a student’s mathematics score from basic profile and preparation details. The project includes a trained regression pipeline, a Flask-based web application, and a polished Streamlit interface for interactive inference.

## Description

This application demonstrates a complete ML workflow from data ingestion to deployment. It reads the student dataset, performs preprocessing, trains and evaluates multiple regression models, and exposes the best-performing model through two user-facing apps:

* a Flask web application for classic browser-based inference
* a Streamlit application with a modern dashboard-style UI

The project is designed to be recruiter-friendly and production-oriented, with a clear separation between data processing, model training, and prediction logic.

## Features

* Predicts a student’s math score using demographic, educational, and preparation inputs
* Automated preprocessing for numeric and categorical features
* Model comparison across multiple regressors with hyperparameter tuning
* Persistent model and preprocessor artifacts saved for inference
* Flask web UI with HTML templates
* Streamlit UI with a polished dashboard theme
* Structured logging and custom exception handling
* Modular codebase for easier maintenance and extension

## Tech Stack

* Python
* Flask
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* CatBoost
* XGBoost
* Seaborn
* Matplotlib
* Dill
* Gunicorn

## Project Architecture

```text
mlproject/
├── application.py               # Flask entry point for browser-based prediction
├── streamlit_app.py             # Streamlit entry point for deployed dashboard UI
├── requirements.txt             # Python dependencies
├── setup.py                     # Package metadata and editable install support
├── artifacts/                   # Generated training data, test data, model, preprocessor
├── logs/                        # Runtime logs created by the custom logger
├── notebook/                    # EDA and training notebooks
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/stud.csv            # Source dataset used for training
├── src/
│   ├── exception.py             # Custom exception wrapper with detailed error messages
│   ├── logger.py                # Central logging configuration
│   ├── utils.py                 # Save/load helpers and model evaluation utility
│   ├── components/
│   │   ├── data_ingestion.py    # Loads dataset and creates train/test splits
│   │   ├── data_transformation.py # Builds preprocessing pipeline
│   │   └── model_trainer.py     # Trains and evaluates candidate models
│   └── pipeline/
│       ├── predict_pipeline.py  # Inference pipeline and custom input wrapper
│       └── train_pipeline.py    # Reserved for orchestration / future training flow
└── templates/
    ├── index.html               # Landing page for Flask UI
    └── home.html                # Prediction form for Flask UI
```

## Data Flow

1. The raw dataset is loaded from `notebook/data/stud.csv`.
2. `DataIngestion` creates an 80/20 train-test split and stores the outputs in `artifacts/`.
3. `DataTransformation` applies:
   * median imputation + standard scaling for numeric columns
   * most-frequent imputation + one-hot encoding + scaling for categorical columns
4. `ModelTrainer` evaluates multiple regressors using cross-validated grid search.
5. The best model is saved to `artifacts/model.pkl` and the fitted preprocessor to `artifacts/preprocessor.pkl`.
6. At inference time, `CustomData` converts user input into a dataframe and `PredictPipeline` transforms the input before generating predictions.

## Installation Instructions

### 1. Clone or open the project

```bash
cd "c:\Users\hariskumar uta\OneDrive\Dokumen\mlproject"
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the Flask application

```bash
python application.py
```

Open the app in your browser:

```text
http://127.0.0.1:5000
```

The prediction form is available at:

```text
http://127.0.0.1:5000/predictdata
```

### Run the Streamlit application

```bash
streamlit run streamlit_app.py
```

This launches the polished dashboard UI and reuses the same trained model artifacts.

## Example / Screenshots

The project includes two user interfaces:

* a Flask-based form UI under `/predictdata`
* a Streamlit dashboard UI with a custom dark theme and modern card layout

If you are presenting this project in a portfolio or resume, include screenshots of both interfaces here.

## Model Details

This project is a supervised regression problem. The target variable is `math_score`.

### Preprocessing

* Numeric features: `reading_score`, `writing_score`
* Categorical features: `gender`, `race_ethnicity`, `parental_level_of_education`, `lunch`, `test_preparation_course`

### Transformation pipeline

* Numeric pipeline: median imputation + `StandardScaler`
* Categorical pipeline: most-frequent imputation + `OneHotEncoder` + scaling

### Model selection

The training pipeline compares several regression models, including:

* Random Forest Regressor
* Decision Tree Regressor
* Gradient Boosting Regressor
* Linear Regression
* K-Neighbors Regressor
* XGBRegressor
* AdaBoost Regressor
* CatBoost Regressor

Each model is tuned with `GridSearchCV`, and the best model is selected based on test-set R2 score. The winning model is serialized to `artifacts/model.pkl`.

## Future Improvements

* Add a dedicated `train_pipeline.py` orchestration script for full one-command retraining
* Add automated unit tests for preprocessing and inference
* Store model metrics and evaluation plots in a report folder
* Add CI/CD for deployment validation
* Introduce a configuration file for dataset and artifact paths
* Add richer UI insights such as feature importance or prediction explanations

## Author / Credits

* Author: Harish
* Email: utaharish78@gmail.com

Built as an end-to-end machine learning project for student performance prediction with Flask and Streamlit deployment options.