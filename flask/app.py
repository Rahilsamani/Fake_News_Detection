from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import nltk
import pickle
import requests
import redis
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime
import os
load_dotenv()

# Download NLTK assets
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Init Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load model and vectorizer
loaded_model = pickle.load(open("model.pkl", 'rb'))
vector = pickle.load(open("vector.pkl", 'rb'))
lemmatizer = WordNetLemmatizer()
stpwrds = set(stopwords.words('english'))

# --- Redis Cloud Configuration ---
cache = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    decode_responses=True,
    username=os.getenv("REDIS_USER"),
    password=os.getenv("REDIS_PASSWORD"),
)

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["fake_news_db"]
predictions_collection = db["predictions"]

# Save Prediction Endpoint
@app.route('/save-prediction', methods=['POST'])
def save_prediction():
    data = request.get_json()
    if not data.get('news_text') or not data.get('predicted_label'):
        return jsonify({'error': 'Missing required fields'}), 400

    doc = {
        "news_text": data['news_text'],
        "source_url": data.get('source_url', None),
        "predicted_label": data['predicted_label'],
        "timestamp": datetime.utcnow()
    }

    predictions_collection.insert_one(doc)
    return jsonify({'message': 'Prediction saved'}), 201

# --- Scraping function ---
def scrape_news_from_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')

        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        heading_text = ' '.join(h.get_text(strip=True) for h in headings)

        paragraphs = soup.find_all('p')
        paragraph_text = ' '.join(p.get_text(strip=True) for p in paragraphs)

        content = f"{heading_text} {paragraph_text}".strip()
        return content if content else None
    except Exception as e:
        print("Scraping error:", e)
        return None

# --- Prediction function ---
def fake_news_det(news):
    review = re.sub(r'[^a-zA-Z\s]', '', news.lower())
    tokens = nltk.word_tokenize(review)
    corpus = [lemmatizer.lemmatize(word) for word in tokens if word not in stpwrds]
    input_data = [' '.join(corpus)]
    vectorized_input_data = vector.transform(input_data)
    prediction = loaded_model.predict(vectorized_input_data)
    return prediction[0]

# --- Routes ---
@app.route('/')
def home():
    return "Fake News Detection API with Redis Cloud Cache"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'news' not in data:
            return jsonify({'error': 'Missing news content'}), 400

        text_input = data['news'].strip()

        # Check if input is a URL
        if text_input.startswith("http://") or text_input.startswith("https://"):
            cached_result = cache.get(text_input)
            if cached_result:
                print("Returning result from Redis cache.")
                return jsonify({'prediction': cached_result}), 200

            content = scrape_news_from_url(text_input)
            if not content:
                return jsonify({'error': 'Unable to scrape content from the URL'}), 500

            result = fake_news_det(content)
            prediction = "Fake" if result == 1 else "Real"

            cache.setex(text_input, 86400, prediction)  # cache for 24 hours
            return jsonify({'prediction': prediction}), 200

        # Text-based prediction
        result = fake_news_det(text_input)
        prediction = "Fake" if result == 1 else "Real"
        return jsonify({'prediction': prediction}), 200

    except Exception as e:
        print("Prediction Error:", e)
        return jsonify({'error': 'Server error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
