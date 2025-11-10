import threading
import webbrowser
from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Load and train the model
df = pd.read_csv("train.csv", sep=";", names=["sentence", "label"], engine="python")
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['sentence'])
y = df['label']
model = MultinomialNB()
model.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    debug_info = None

    if request.method == 'POST':
        sentence = request.form.get('sentence', '')
        new_vector = vectorizer.transform([sentence])
        raw_prediction = model.predict(new_vector)[0]

        # DEBUG: see exactly what the model returned
        print("DEBUG raw_prediction:", repr(raw_prediction), " type:", type(raw_prediction))

        # Normalize raw prediction to a string
        if isinstance(raw_prediction, (bytes, bytearray)):
            label = raw_prediction.decode('utf-8', errors='ignore')
        else:
            label = str(raw_prediction)

        label_norm = label.strip().lower()

        # Map common variants/synonyms to canonical labels
        SYNONYMS = {
            "anger": "angry",
            "happiness": "happy",
            "joy": "happy",
            "sadness": "sad",
            "neutrality": "neutral",
            "fearful": "fear",
            "disgusted": "disgust"
        }
        label_norm = SYNONYMS.get(label_norm, label_norm)

        # Emoji map (keys must be lowercase canonical labels)
        EMOJIS = {
            "happy": "😄",
            "sad": "😢",
            "angry": "😡",
            "neutral": "😐",
            "surprised": "😲",
            "fear": "😨",
            "disgust": "🤢",
            "excited": "🤩",
            "bored": "🥱",
            "love": "❤️"
        }

        # Get emoji (fallback if unknown)
        emoji = EMOJIS.get(label_norm, "🙂")

        # Build display string (capitalized label + emoji)
        display_label = label_norm.capitalize() if label_norm else "Unknown"
        prediction = f"{display_label} {emoji}"

        # optional debug info sent to template
        debug_info = f"raw={repr(raw_prediction)}, normalized='{label_norm}'"

    return render_template('index.html', prediction=prediction, debug=debug_info)


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    # Only open browser if NOT the reloader process
    import os
    if not os.environ.get("WERKZEUG_RUN_MAIN"):  
        threading.Timer(1.0, open_browser).start()

    app.run(debug=True)