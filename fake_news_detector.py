from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class FakeNewsDetector:
    def __init__(self, model_name='bert-base-uncased'):
        self.model_version = "1.0.0"
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
        
    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        outputs = self.model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        return 'fake' if predictions[0][1].item() > 0.5 else 'real'
    
    def get_confidence_score(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        outputs = self.model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        return predictions[0].tolist()
