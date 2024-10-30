import hashlib
import json
from time import time

class Blockchain:
    def __init__(self, detector):
        self.detector = detector
        self.chain = []
        self.current_data = []

        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'data': self.current_data,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.current_data = []
        self.chain.append(block)
        return block

    def new_data(self, author, content, verification):
        self.current_data.append({
            'author': author,
            'content': content,
            'verification': {
                'result': verification,
                'confidence_score': self.detector.get_confidence_score(content),
                'timestamp': time()
            }
        })

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
