from datasets import load_dataset
from transformers import Trainer, TrainingArguments

dataset = load_dataset("fake_news")
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    evaluation_strategy="epoch"
)
