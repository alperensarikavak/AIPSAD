import joblib

model = joblib.load('models/email_random_forest_model.pkl')
vectorizer = joblib.load('models/email_tfidf_vectorizer.pkl')

messages = [
    "Free entry in 2 a wkly comp to win FA Cup final tkts",
    "ALPO123.",
    "Are we still meeting at 6pm today?",
    "xxxxxxx."
]

X = vectorizer.transform(messages)
probas = model.predict_proba(X)

for msg, proba in zip(messages, probas):
    print(f"{msg[:40]} → Spam probability: {proba[1]*100:.2f}%")
