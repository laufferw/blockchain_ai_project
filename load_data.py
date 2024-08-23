import pandas as pd

# Load the real and fake news datasets
real_news_df = pd.read_csv(r'/users/william.laufferpostman.com/repos/blockchain_ai_project/News_dataset/True.csv')
fake_news_df = pd.read_csv(r'/users/william.laufferpostman.com/repos/blockchain_ai_project/News_dataset/Fake.csv')

# Display the first few rows of each dataset to verify loading
print("Real News Data:")
print(real_news_df.head())

print("\nFake News Data:")
print(fake_news_df.head())