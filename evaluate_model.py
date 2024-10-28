from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
from fake_news_detector import FakeNewsDetector

def evaluate_model():
    detector = FakeNewsDetector()
    
    # Test data
    test_texts = [
        "Breaking: Scientists confirm water is wet in groundbreaking study",
        "Aliens secretly control all world governments, insider reveals",
        "Local community opens new public library",
        "Study shows exercise and balanced diet improve health",
        "Secret pizza ingredient makes you immortal, doctors hate this!"
    ]
    
    test_labels = ["real", "fake", "real", "real", "fake"]
    
    predictions = [detector.predict(text) for text in test_texts]
    
    print("Model Evaluation Results:")
    print("-" * 50)
    print("\nClassification Report:")
    print(classification_report(test_labels, predictions))
    print("\nConfusion Matrix:")
    print(confusion_matrix(test_labels, predictions))
    
    # Print individual predictions
    print("\nDetailed Predictions:")
    for text, pred, true in zip(test_texts, predictions, test_labels):
        print(f"\nText: {text[:50]}...")
        print(f"Predicted: {pred}")
        print(f"Actual: {true}")

if __name__ == "__main__":
    evaluate_model()
