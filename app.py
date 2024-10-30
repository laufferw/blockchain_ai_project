from flask import Flask, request, jsonify, render_template
from blockchain import Blockchain
from fake_news_detector import FakeNewsDetector

app = Flask(__name__)

blockchain = Blockchain()
detector = FakeNewsDetector()

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
        return jsonify({'error': str(e)}), 500
@app.route('/chain', methods=['GET'])
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
    app,
    key_func=get_remote_address,
    default_limits=["100 per day", "10 per hour"]
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
