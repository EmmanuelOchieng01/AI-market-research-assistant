# AI Market Research Assistant

An intelligent system for scraping, analyzing, and summarizing global commodity and agriculture news using Natural Language Processing and sentiment analysis.

## Features

- Multi-source web scraping from RSS feeds
- Automated article summarization using NLP
- Real-time sentiment analysis (positive/negative/neutral)
- Named Entity Recognition for commodities, companies, and locations
- Trend detection and keyword extraction
- Automated daily/weekly market digest reports
- Interactive web dashboard with charts and filtering
- SQLite database for efficient article storage

## Technology Stack

**Backend:**
- Flask - Web framework
- BeautifulSoup4 - HTML parsing
- Feedparser - RSS feed processing
- NLTK - Natural language processing
- VADER - Sentiment analysis

**Frontend:**
- HTML5/CSS3/JavaScript
- Plotly.js - Interactive charts
- Responsive design

**Database:**
- SQLite - Article storage and retrieval

## Installation

```bash
pip install -r requirements.txt
python src/download_models.py
python app.py
```

Visit `http://localhost:5000` to access the dashboard.

## Usage

1. Click "Scrape News" to fetch latest articles from configured sources
2. View articles with sentiment scores and summaries
3. Filter by sentiment (positive/negative/neutral) or date range
4. Generate market digest reports with key insights
5. Analyze custom text using the NLP pipeline

## Project Structure

```
ai_market_research/
├── app.py                    # Main Flask application
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── src/
│   ├── scraper.py           # Web scraping logic
│   ├── nlp_processor.py     # Text processing
│   ├── summarizer.py        # Article summarization
│   ├── sentiment.py         # Sentiment analysis
│   ├── entity_extractor.py  # Named entity recognition
│   ├── digest_generator.py  # Report generation
│   └── database.py          # Database operations
├── templates/
│   └── index.html           # Web interface
└── static/
    ├── css/style.css        # Styling
    └── js/app.js            # Frontend logic
```

## License

MIT License
