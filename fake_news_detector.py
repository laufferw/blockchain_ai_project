from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import logging  # Added missing import

class FakeNewsDetector:
    def __init__(self, model_name='bert-base-uncased'):
        self.model_version = "1.0.0"
        
        # Configure logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Add handler if none exists to avoid duplicate logs
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        
        # Load model and tokenizer
        self.logger.info(f"Initializing FakeNewsDetector with model: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
        self.logger.info("Model and tokenizer loaded successfully")
        
    def predict(self, text):
        self.logger.debug(f"Predicting for text: {text[:100]}...")
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        outputs = self.model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        result = 'fake' if predictions[0][1].item() > 0.5 else 'real'
        self.logger.info(f"Prediction: {result}")
        return result
    
    def get_confidence_score(self, text):
        self.logger.debug(f"Getting confidence score for text: {text[:100]}...")
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        outputs = self.model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        scores = predictions[0].tolist()
        self.logger.info(f"Confidence scores: real={scores[0]:.3f}, fake={scores[1]:.3f}")
        return scores