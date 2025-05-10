# Flask Spam Predictor

This project is a Flask web application that predicts the probability of a message being spam using a pre-trained machine learning model. The application provides a simple interface for users to input messages and receive spam probability predictions.

## Project Structure

```
flask-spam-predictor
├── app.py                # Main entry point of the Flask application
├── static
│   └── style.css         # CSS styles for the web application
├── templates
│   └── index.html        # HTML template for user input
├── models
│   └── spam_model.pkl     # Pre-trained Random Forest model for spam detection
├── requirements.txt       # List of dependencies for the project
└── README.md              # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-spam-predictor
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python app.py
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Enter a message in the input field and click the "Check Spam" button.
- The application will process the input and display the predicted spam probability.

## Dependencies

- Flask
- scikit-learn
- pandas
- numpy

## License

This project is licensed under the MIT License.