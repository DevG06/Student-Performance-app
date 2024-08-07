# Student Performance Analysis

## Table of Contents

- [Project Overview](#project-overview)
- [Objectvies](#objectives)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [License](#license)

## Project Overview

The Student Performance Analysis and Prediction project is an end-to-end machine learning application designed to analyze and predict students' performance in school based on various demographic and academic factors. The primary goal is to predict a student's math score using regression models, leveraging multiple features such as race, gender, reading score, writing score, and more. 

## Objectives

1. **Data Analysis and Visualization**:
   - Utilize data visualization tools to understand the relationship between different variables and student performance.
   - Identify key factors that influence student performance through exploratory data analysis (EDA).

2. **Data Preprocessing**:
   - Implement data cleaning and transformation techniques to prepare the dataset for model training.
   - Handle missing values, encode categorical variables, and normalize numerical features to improve model accuracy.

3. **Model Training and Evaluation**:
   - Train various regression models using libraries like Sklearn, XGBoost, and CatBoost.
   - Evaluate the performance of the models using R2_score.
   - Select the best-performing model for deployment.

4. **Web Application Development**:
   - Develop a backend using Flask to serve the model and handle user inputs.
   - Design a user-friendly frontend with HTML and CSS for users to interact with the application.
   - Implement functionalities for users to input data and receive predicted math scores.

5. **Error Handling and Logging**:
   - Create a custom exception handler to manage errors gracefully and provide meaningful error messages.
   - Implement a logging mechanism to record application activities and errors for debugging and monitoring purposes.

6. **Deployment**:
   - Deploy the application on AWS EC2 using Docker and AWS ECR to make it accessible to users.
   - Set up a CI/CD pipeline using GitHub Actions to automate testing, building, and deployment processes.

## Project Structure

├── .github/workflows  # CI/CD workflows
├── artifacts          # Model artifacts and other files
├── notebook           # Jupyter notebooks for EDA and training
├── src                # Source code
│   ├── __init__.py
│   ├── components     # Data ingestion, transformation and training scripts 
│   ├── pipeline       # Model training and prediction pipeline
│   ├── utils.py       # Utility functions
│   ├── exceptions.py  # Custom exceptions
│   └── logger.py      # Custom logger
├── templates          # HTML templates for the frontend
├── .gitignore
├── Dockerfile
├── README.md
├── app.py             # Main Flask application
├── requirements.txt   # Python dependencies
└── setup.py           # Setup script

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

