import joblib

class FakeNewsDetector:
    def __init__(self, model_path='/users/william.laufferpostman.com/repos/blockchain_ai_project/models/fake_news_detector.pkl'):
        # Load the pre-trained model
        self.model = joblib.load(model_path)

    def predict(self, text):
        # Predict whether the input text is real or fake
        result = self.model.predict([text])
        return 'fake' if result[0] == 1 else 'real'
