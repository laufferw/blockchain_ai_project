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

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
