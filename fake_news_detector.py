from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pandas as pd

class FakeNewsDetector:
    def __init__(self):
        self.model = self.train_model()

    def train_model(self):
        # Existing data
        data = {
            'text': [
                "This is real news", 
                "This is fake news", 
                "Another real article", 
                "More fake content"
            ],
            'label': [0, 1, 0, 1]  # 0 for real, 1 for fake
        }

        # Add the misclassified transcript to the training data
        data['text'].append("Full transcript of the presidential speech")
        data['label'].append(0)  # Label it as real

        df = pd.DataFrame(data)

        model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        model.fit(df['text'], df['label'])

        return model

    def predict(self, text):
        result = self.model.predict([text])
        return 'fake' if result[0] == 1 else 'real'
