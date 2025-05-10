from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Email modeli ve vectorizer
email_model = joblib.load('models/email_random_forest_model.pkl')
email_vectorizer = joblib.load('models/email_tfidf_vectorizer.pkl')

# SMS modeli ve vectorizer
sms_model = joblib.load('models/sms_random_forest_model.pkl')
sms_vectorizer = joblib.load('models/sms_tfidf_vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = ''
    proba_percent = None

    if request.method == 'POST':
        message = request.form['message']
        message_type = request.form['message_type']

        if message_type == 'sms':
            message_vector = sms_vectorizer.transform([message])
            proba = sms_model.predict_proba(message_vector)[0][1]
        else:  # message_type == 'email'
            message_vector = email_vectorizer.transform([message])
            proba = email_model.predict_proba(message_vector)[0][1]

        proba_percent = round(proba * 100, 2)

        if proba_percent >= 70:
            prediction_text = f"This message is classified as SPAM ({proba_percent}%)"
        else:
            prediction_text = f"This message is classified as NOT SPAM ({proba_percent}%)"

    return render_template('index.html', prediction_text=prediction_text, proba_percent=proba_percent)

if __name__ == '__main__':
    app.run(debug=True)
