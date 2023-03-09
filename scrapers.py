import snscrape.modules.twitter as sntwitter
from sqlalchemy.orm import Session
from database import engine
import models


def get_tweets(account):
  query = f"(from:{account}) since:2023-02-01 -filter:replies"
  for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    session = Session(engine)
    result = session.query(models.Tweets).filter(
              models.Tweets.id == tweet.id).first()
    if result == None:
      tweet_model = models.Tweets(
                  id = tweet.id,
                  date = tweet.date,
                  username = tweet.user.username,
                  content = tweet.rawContent)
      session.add(tweet_model)
      session.commit()


def get_replies(account):
  query = "(to:elonmusk) since:2023-02-01"
  for reply in sntwitter.TwitterSearchScraper(query).get_items():
    session = Session(engine)
    result = session.query(models.Replies).filter(
              models.Replies.id == reply.id).first()
    if result == None:
      reply_model = models.Replies(
                  id = reply.id,
                  date = reply.date,
                  username = reply.user.username,
                  content = reply.rawContent)
      session.add(reply_model)
      session.commit()
