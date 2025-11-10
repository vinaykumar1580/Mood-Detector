import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

class MoodDetector:
    def __init__(self, model_path='model.pkl', data_path='train.csv'):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()
        self.load_data(data_path)
        self.load_model(model_path)

    def load_data(self, data_path):
        df = pd.read_csv(data_path, sep=";", names=["sentence", "label"], engine="python")
        self.X = self.vectorizer.fit_transform(df['sentence'])
        self.y = df['label']

    def train_model(self):
        self.model.fit(self.X, self.y)
        joblib.dump(self.model, 'model.pkl')
        joblib.dump(self.vectorizer, 'vectorizer.pkl')

    def predict_mood(self, sentence):
        new_vector = self.vectorizer.transform([sentence])
        prediction = self.model.predict(new_vector)
        return prediction[0]

    def load_model(self, model_path):
        try:
            self.model = joblib.load(model_path)
            self.vectorizer = joblib.load('vectorizer.pkl')
        except FileNotFoundError:
            print("Model not found. Please train the model first.")