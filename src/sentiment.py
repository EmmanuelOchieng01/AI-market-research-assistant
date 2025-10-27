"""
Sentiment analysis using VADER
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    """Analyzes sentiment of news articles"""

    def __init__(self):
        """Initialize VADER sentiment analyzer"""
        self.vader = SentimentIntensityAnalyzer()

    def analyze(self, text):
        """
        Analyze sentiment of text

        Args:
            text (str): Input text

        Returns:
            dict: Sentiment scores and label
        """
        vader_scores = self.vader.polarity_scores(text)
        compound_score = vader_scores['compound']

        # Classify sentiment
        if compound_score >= 0.2:
            label = 'positive'
        elif compound_score <= -0.2:
            label = 'negative'
        else:
            label = 'neutral'

        return {
            'score': round(compound_score, 3),
            'label': label,
            'positive': round(vader_scores['pos'], 3),
            'negative': round(vader_scores['neg'], 3),
            'neutral': round(vader_scores['neu'], 3)
        }

    def get_sentiment_trend(self, sentiments):
        """
        Calculate overall sentiment trend

        Args:
            sentiments (list): List of sentiment dictionaries

        Returns:
            dict: Trend summary
        """
        if not sentiments:
            return {'trend': 'neutral', 'average': 0}

        avg_score = sum(s['score'] for s in sentiments) / len(sentiments)

        if avg_score >= 0.2:
            trend = 'bullish'
        elif avg_score <= -0.2:
            trend = 'bearish'
        else:
            trend = 'neutral'

        return {
            'trend': trend,
            'average': round(avg_score, 3),
            'distribution': {
                'positive': sum(1 for s in sentiments if s['label'] == 'positive'),
                'negative': sum(1 for s in sentiments if s['label'] == 'negative'),
                'neutral': sum(1 for s in sentiments if s['label'] == 'neutral')
            }
        }
