# Standard library imports
import os
import logging
import time
from typing import Any, Dict

# Third-party imports
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from waitress import serve
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# =====================
# Configuration
# =====================
MODEL_FILENAME = 'trained_model.pkl'
HTML_FILENAME = 'chatbot_client.html'
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5001
SIMILARITY_THRESHOLD = 0.4

# =====================
# Logging Setup
# =====================
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
logger = logging.getLogger(__name__)

# =====================
# Flask App Setup
# =====================
app = Flask(__name__)
CORS(app)

# =====================
# Model Loading
# =====================
logger.info("Loading trained model...")
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), MODEL_FILENAME)
try:
    with open(model_path, 'rb') as f:
        model_data = pickle.load(f)
    logger.info("Model loaded successfully!")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    raise

# =====================
# Utility Functions
# =====================
def find_answer(question: str) -> str:
    """Find the best answer for a given question using cosine similarity."""
    question_vector = model_data['vectorizer'].transform([question.lower()])
    similarities = cosine_similarity(question_vector, model_data['question_vectors'])[0]
    best_match_idx = int(np.argmax(similarities))
    best_score = float(similarities[best_match_idx])
    if best_score < SIMILARITY_THRESHOLD:
        return "I'm sorry, I couldn't find an answer to your question."
    return model_data['answers'][best_match_idx]

# =====================
# API Endpoints
# =====================
@app.route('/chatbot', methods=['POST'])
def chatbot() -> Any:
    """Chatbot Q&A endpoint."""
    try:
        data: Dict = request.get_json(force=True, silent=True) or {}
        logger.info(f"Received data: {data}")
        question = data.get('question')
        if not question or not isinstance(question, str):
            logger.warning("No valid 'question' provided in request.")
            return jsonify({'error': "No valid 'question' provided."}), 400
        start_time = time.time()
        answer = find_answer(question)
        end_time = time.time()
        response = {
            'answer': answer,
            'response_time': f"{(end_time - start_time)*1000:.2f} milliseconds"
        }
        return jsonify(response)
    except Exception as e:
        logger.error(f"Error in /chatbot: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check() -> Any:
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'message': 'Chatbot server is running'})

@app.route('/ready', methods=['GET'])
def readiness_check() -> Any:
    """Readiness check endpoint."""
    # Here you could add checks for model, DB, etc.
    try:
        _ = model_data['vectorizer']
        _ = model_data['question_vectors']
        _ = model_data['answers']
        return jsonify({'status': 'ready'}), 200
    except Exception as e:
        logger.error(f"Readiness check failed: {e}")
        return jsonify({'status': 'not ready', 'error': str(e)}), 500

@app.route('/')
def serve_chatbot_client() -> Any:
    """Serve the chatbot client HTML file."""
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), HTML_FILENAME)
    if not os.path.exists(html_path):
        logger.error(f"HTML file not found: {html_path}")
        return jsonify({'error': 'Chatbot client HTML not found.'}), 404
    return send_file(html_path)

# =====================
# Main Entrypoint
# =====================
if __name__ == '__main__':
    logger.info(f"✅ Microservice Flask app running with Waitress on {SERVER_HOST}:{SERVER_PORT} ...")
    serve(app, host=SERVER_HOST, port=SERVER_PORT)

 