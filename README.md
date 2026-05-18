# Student Exam Performance Predictor

🚀 **Live Demo:** https://studentscorepredictor-ml.streamlit.app/

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

An end-to-end Machine Learning project that predicts a student’s mathematics score using demographic, educational, and preparation-related inputs. The project demonstrates a complete ML workflow including preprocessing, model training, evaluation, deployment, containerization, and cloud deployment.

---

# Deployment

This project was successfully deployed using multiple deployment platforms and cloud technologies:

- ✅ Streamlit Community Cloud (currently active deployment)
- ✅ AWS Elastic Beanstalk deployment for Flask application hosting
- ✅ Dockerized deployment using:
  - Amazon EC2
  - Amazon ECR (Elastic Container Registry)
  - Docker containers

The AWS EC2 + ECR deployment was tested successfully during development and learning phases. Due to higher cloud infrastructure costs, the public production deployment is currently maintained on Streamlit Cloud.

---

# Description

This application demonstrates a complete Machine Learning workflow from data ingestion to deployment. It reads the student dataset, performs preprocessing, trains and evaluates multiple regression models, and exposes the best-performing model through two user-facing applications:

- A Flask web application for browser-based inference
- A Streamlit dashboard application with a modern interactive UI

The project is designed to be recruiter-friendly and production-oriented, with a clear separation between data processing, model training, prediction pipelines, and deployment logic.

This project demonstrates:
- End-to-end ML workflow
- Feature engineering and preprocessing
- Model selection and hyperparameter tuning
- Web application development
- Docker containerization
- AWS deployment
- Streamlit cloud deployment

---

# Features

- Predicts student mathematics scores using demographic and academic inputs
- Automated preprocessing for categorical and numerical features
- Multiple regression model comparison with hyperparameter tuning
- Persistent model and preprocessor artifacts for inference
- Flask-based web application
- Streamlit interactive dashboard UI
- Structured logging and exception handling
- Modular and scalable project architecture
- Cloud deployment support
- Dockerized deployment workflow

---

# Tech Stack

## Machine Learning & Backend
- Python
- Scikit-learn
- Flask
- Streamlit

## Data Analysis & Visualization
- Pandas
- NumPy
- Matplotlib
- Seaborn

## ML Models
- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- K-Neighbors Regressor
- XGBoost
- AdaBoost Regressor
- CatBoost Regressor

## Deployment & Cloud
- AWS Elastic Beanstalk
- AWS EC2
- AWS ECR
- Docker
- Gunicorn

## Utilities
- Dill

---

# Project Architecture

```text
mlproject/
├── application.py               # Flask entry point for browser-based prediction
├── streamlit_app.py             # Streamlit entry point for deployed dashboard UI
├── requirements.txt             # Python dependencies
├── setup.py                     # Package metadata and editable install support
├── artifacts/                   # Generated training data, model, preprocessor
├── logs/                        # Runtime logs
├── notebook/                    # EDA and model training notebooks
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/stud.csv
├── src/
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   └── pipeline/
│       ├── predict_pipeline.py
│       └── train_pipeline.py
└── templates/
    ├── index.html
    └── home.html
```

---

# Data Flow

1. The raw dataset is loaded from `notebook/data/stud.csv`
2. `DataIngestion` creates train-test splits
3. `DataTransformation` performs:
   - Median imputation
   - Standard scaling
   - One-hot encoding
4. `ModelTrainer` evaluates multiple regression models
5. The best model is saved into:
   - `artifacts/model.pkl`
   - `artifacts/preprocessor.pkl`
6. During inference:
   - User input is converted into a dataframe
   - Preprocessing pipeline is applied
   - Final prediction is generated

---

# Installation Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows PowerShell

```bash
venv\Scripts\Activate.ps1
```

### Linux / MacOS

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

## Run Flask Application

```bash
python application.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

Prediction route:

```text
http://127.0.0.1:5000/predictdata
```

---

## Run Streamlit Application

```bash
streamlit run streamlit_app.py
```

---

# Docker Deployment

## Build Docker Image

```bash
docker build -t student-performance-predictor .
```

## Run Docker Container

```bash
docker run -p 8501:8501 student-performance-predictor
```

---

# AWS Deployment

The project was tested and deployed using:

- AWS Elastic Beanstalk
- AWS EC2
- AWS ECR
- Docker containers

Deployment workflow included:
- Docker image creation
- Image push to Amazon ECR
- Container deployment on EC2
- Gunicorn-based production serving

---

# Model Details

This project is a supervised regression problem where:

- **Target Variable:** `math_score`

## Features Used

### Numerical Features
- `reading_score`
- `writing_score`

### Categorical Features
- `gender`
- `race_ethnicity`
- `parental_level_of_education`
- `lunch`
- `test_preparation_course`

---

# Transformation Pipeline

## Numerical Pipeline
- Median Imputation
- StandardScaler

## Categorical Pipeline
- Most Frequent Imputation
- OneHotEncoder
- StandardScaler

---

# Model Selection

The training pipeline compares multiple regression algorithms using `GridSearchCV`.

Models evaluated:
- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- K-Neighbors Regressor
- XGBRegressor
- AdaBoost Regressor
- CatBoost Regressor

The best-performing model is selected using the highest R² score and saved for inference.

---

# Example / Screenshots

The project contains:
- Flask-based prediction UI
- Streamlit interactive dashboard UI

You can add screenshots here for:
- Home page
- Prediction dashboard
- Model output
- Streamlit deployment

---

# Future Improvements

- Add CI/CD pipelines using GitHub Actions
- Add unit and integration testing
- Add feature importance visualization
- Add model explainability using SHAP
- Add retraining orchestration pipeline
- Improve monitoring and logging
- Deploy using Kubernetes

---

# Author

## Harish

- GitHub: https://github.com/Harish-Uta17
- Email: utaharish78@gmail.com

Built as an end-to-end Machine Learning project demonstrating ML engineering, deployment, Docker, and AWS cloud deployment workflows.

---

# License

This project is open-source and available for educational and learning purposes.