import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Step 1: Download NLTK stopwords (only need to do this once)
nltk.download('stopwords')

# Step 2: Initialize the stemmer and stop words
ps = PorterStemmer()  # Stemmer to reduce words to their root form
stop_words = set(stopwords.words('english'))  # List of stop words in English

# Step 3: Define the preprocessing function
def preprocess(text):
    # Remove non-alphabetic characters
    text = re.sub('[^a-zA-Z]', ' ', text)
    # Convert text to lowercase
    text = text.lower()
    # Tokenize and remove stop words
    words = text.split()
    words = [ps.stem(word) for word in words if word not in stop_words]
    # Join the words back into a single string
    return ' '.join(words)

# Step 4: Load the real and fake news datasets
real_news_df = pd.read_csv(r'/users/william.laufferpostman.com/repos/blockchain_ai_project/News_dataset/True.csv')
fake_news_df = pd.read_csv(r'/users/william.laufferpostman.com/repos/blockchain_ai_project/News_dataset/Fake.csv')

# Step 5: Add a 'label' column: 0 for real news, 1 for fake news
real_news_df['label'] = 0
fake_news_df['label'] = 1

# Step 6: Combine the real and fake news DataFrames
df = pd.concat([real_news_df, fake_news_df], ignore_index=True)

# Step 7: Apply the preprocessing function to the 'text' column
df['cleaned_text'] = df['text'].apply(preprocess)

# Step 8: Display the first few rows of the preprocessed data
print("Preprocessed Dataset:")
print(df[['text', 'cleaned_text', 'label']].head())

# Step 9: Save the preprocessed dataset to a new CSV file (optional)
df.to_csv(r'/users/william.laufferpostman.com/repos/blockchain_ai_project/News_dataset/preprocessed_news.csv', index=False)
