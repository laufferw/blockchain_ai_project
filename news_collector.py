from newspaper import Article, build
import requests
from datetime import datetime

class NewsCollector:
    def __init__(self):
        self.sources = [
            'https://reuters.com',
            'https://apnews.com',
            'https://bloomberg.com'
        ]
    
    def collect_articles(self, limit=10):
        collected_news = []
        for source in self.sources:
            paper = build(source, memoize_articles=False)
            for article in paper.articles[:limit]:
                try:
                    article.download()
                    article.parse()
                    news_item = {
                        'author': article.authors[0] if article.authors else 'Unknown',
                        'content': article.text,
                        'title': article.title,
                        'url': article.url,
                        'timestamp': datetime.now().isoformat()
                    }
                    collected_news.append(news_item)
                except Exception as e:
                    continue
        return collected_news
