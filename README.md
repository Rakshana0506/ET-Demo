# Wellness Predictor App

A Flask-based web application that predicts a user's wellness status based on their sleep hours and screen time, using a trained machine learning model.

## Features
- **User Authentication**: Sign up, log in, and log out securely (stored locally for demo purposes).
- **Wellness Prediction**: Enter your daily sleep hours and screen time to receive a prediction.
- **Activity Logging**: All user actions are logged with timestamps.
- **Machine Learning Model**: Model trained with scikit-learn and stored as a `.pkl` file.
- **Local Deployment**: Run locally using Python and Flask.

## Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML (Jinja2 templates)
- **Machine Learning**: scikit-learn, NumPy, pandas
- **Storage**: Local text files for users and logs, Pickle for ML model

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rakshana0506/ET-Demo.git
   cd ET-Demo
## Usage

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the application:
   ```bash
   python webapp.py
The app will be available at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

3. Example usage:
- Enter your sleep hours and daily screen time in the form.
- Click "Predict" to see your wellness status.


