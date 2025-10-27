"""
Configuration settings for the AI Market Research Assistant
"""

# RSS feed URLs for news sources
NEWS_SOURCES = {
    'reuters_commodities': 'https://www.reuters.com/markets/commodities/rss',
    'bloomberg_agriculture': 'https://www.bloomberg.com/feeds/agriculture.rss',
}

# List of commodities to track
COMMODITIES = [
    'corn', 'wheat', 'soybeans', 'rice', 'coffee', 'cotton',
    'sugar', 'cocoa', 'cattle', 'hogs', 'gold', 'oil', 'copper'
]

# NLP settings
NLP_CONFIG = {
    'max_summary_length': 150,
    'min_summary_length': 50,
    'top_keywords': 10,
}

# Web scraping settings
SCRAPING_CONFIG = {
    'user_agent': 'Mozilla/5.0 (Market Research Bot)',
    'request_delay': 2,
    'timeout': 30,
    'max_articles_per_source': 50,
}

# Sentiment thresholds
SENTIMENT_THRESHOLDS = {
    'positive': 0.2,
    'negative': -0.2,
}

# Database configuration
DATABASE_PATH = 'data/articles.db'
