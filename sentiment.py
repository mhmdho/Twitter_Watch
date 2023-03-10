from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

def sentiment_analyzer(text):
  word_mention = r'@\w+'
  word_link = r'http\S+'
  word_link2 = r'www.\S+'
  text = re.sub(word_mention, '@user', text)
  text = re.sub(word_link, 'http', text)
  text = re.sub(word_link2, 'http', text)

  analyzer = SentimentIntensityAnalyzer()
  result = analyzer.polarity_scores(text)['compound']

  return result
