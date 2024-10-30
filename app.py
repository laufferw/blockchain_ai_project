from flask import Flask, request, jsonify, render_template
from blockchain import Blockchain
from fake_news_detector import FakeNewsDetector



app = Flask(__name__)
# Initialize components
detector = Detector()  # Make sure this is properly imported
blockchain = Blockchain(detector=detector)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        values = request.get_json()
        required = ['author', 'content']
        if not all(k in values for k in required):
            return 'Missing values', 400

        verification = detector.predict(values['content'])
        
        # Add logging here
        print(f"Values received: {values}")
        print(f"Verification result: {verification}")
        
        index = blockchain.new_data(values['author'], values['content'], verification)
        
        last_proof = blockchain.last_block['proof']
        proof = blockchain.proof_of_work(last_proof)
        previous_hash = blockchain.hash(blockchain.last_block)
        block = blockchain.new_block(proof, previous_hash)

        response = {
            'message': f'Data will be added to Block {index}',
            'block': block,
        }
        return jsonify(response), 201
    except Exception as e:
        print(f"Error in submit_data: {str(e)}")  # Add detailed error logging
        return jsonify({'error': str(e)}), 500@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Fake News Detection API"
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,  # Explicitly name the app parameter
    key_func=get_remote_address,
    default_limits=["100 per day", "10 per hour"],
    storage_uri="memory://"  # Adding storage configuration
)

@app.route('/api/key', methods=['POST'])
def generate_api_key():
    values = request.get_json()
    if 'email' not in values:
        return jsonify({'error': 'Please provide email'}), 400
    api_key = generate_unique_key()  # Implement this function
    return jsonify({'api_key': api_key}), 201

from flask_cors import CORS

CORS(app)

from news_collector import NewsCollector

news_collector = NewsCollector()

@app.route('/collect', methods=['POST'])
def collect_news():
    try:
        articles = news_collector.collect_articles()
        for article in articles:
            verification = detector.predict(article['content'])
            blockchain.new_data(article['author'], article['content'], verification)
        
        response = {
            'message': f'Collected and processed {len(articles)} articles',
            'articles_count': len(articles)
        }
        return jsonify(response), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update your environment variable setting
import os
os.environ['FLASK_DEBUG'] = '1'
bash
import os
os.environ['FLASK_DEBUG'] = '1'
