# Heart Disease Detection using Machine Learning Web Application

## Overview

This is a web-based **Heart Disease Detection** project built using **Flask** and **Python**. The application helps predict the likelihood of heart disease based on various medical parameters. The user inputs the required details, and the model provides a prediction on whether the person has heart disease or not.

## Features

- **User-friendly Web Interface**: Built with Flask for smooth interaction.
- **Heart Disease Prediction**: Users can input medical details, and the model predicts the likelihood of heart disease.
- **Real-time Predictions**: Provides fast, real-time predictions based on user input.
- **Deployed on Vercel**: Access the live application here: [Heart Disease Detection](https://varunheart-disease-detection.vercel.app)

## Tech Stack

- **Backend**: Flask (Python Web Framework)
- **Machine Learning**: Python Libraries (e.g., scikit-learn, pandas, numpy) for building the heart disease prediction model
- **Deployment**: Vercel
- **Frontend**: HTML, CSS 

## Setup Instructions

### 1. Clone the Repository

Clone the project to your local machine using the following command:

```bash
git clone https://github.com/yourusername/heart-disease-detection.git

```

2. Set up a Virtual Environment
Navigate to the project folder and create a virtual environment:

```bash
cd heart-disease-detection
python3 -m venv venv
```
Activate the virtual environment:

On Windows:
```bash
.\venv\Scripts\activate
```
3. Install Dependencies
Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Application
Start the Flask app:
```bash
flask run
```
The application will be available at http://127.0.0.1:5000/ on your local machine.
Model Information
The heart disease prediction model is built using machine learning algorithms. The model is trained on a dataset containing medical records, and it uses factors like age, blood pressure, cholesterol levels, and others to predict the likelihood of heart disease.

Contributing
Feel free to fork this repository, contribute, and submit pull requests. Please make sure to follow the coding standards and guidelines provided.



