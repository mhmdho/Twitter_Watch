import snscrape.modules.twitter as sntwitter
import models
from database import engine
from sqlalchemy.orm import Session
from sentiment import sentiment_analyzer


def get_accounts(accounts_list:list):
  for account in accounts_list:
    profile = sntwitter.TwitterUserScraper(account).entity
    session = Session(engine)
    result = session.query(models.Accounts).filter(
              models.Accounts.username == account.lower()).first()
    if result == None:
      weblink = label_desc = label_url = None
      if profile.link:
        weblink = profile.link.url
      if profile.label:
        label_desc = profile.label.description
        label_url = profile.label.url
      account_model = models.Accounts(
                  username = account.lower(),
                  name = profile.displayname,
                  description = profile.renderedDescription,
                  verified = profile.verified,
                  created_at = profile.created,
                  followers_count = profile.followersCount,
                  friends_count = profile.friendsCount,
                  location = profile.location,
                  image = (profile.profileImageUrl).replace('normal', '400x400'),
                  tweets_count = profile.statusesCount,
                  weblink = weblink,
                  label_desc = label_desc,
                  label_url = label_url,
      )
      session.add(account_model)
      session.commit()


def get_tweets(account):
  session = Session(engine)
  the_account = session.query(models.Accounts).filter(
                  models.Accounts.username == account.lower()).first()
  if the_account:
    query = f"(from:{account}) since:2023-02-01 -filter:replies"
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
      result = session.query(models.Tweets).filter(
                models.Tweets.id == tweet.id).first()
      if result == None:
        tweet_model = models.Tweets(
                    id = tweet.id,
                    date = tweet.date,
                    username = tweet.user.username,
                    content = tweet.rawContent,
                    sentiment = sentiment_analyzer(tweet.rawContent),
                    owner_id = the_account.id)
        session.add(tweet_model)
        session.commit()


def get_replies(account):
  session = Session(engine)
  the_account = session.query(models.Accounts).filter(
                  models.Accounts.username == account.lower()).first()
  if the_account:
    query = f"(to:{account}) since:2023-02-01"
    for reply in sntwitter.TwitterSearchScraper(query).get_items():
      session = Session(engine)
      result = session.query(models.Replies).filter(
                models.Replies.id == reply.id).first()
      if result == None:
        reply_model = models.Replies(
                    id = reply.id,
                    date = reply.date,
                    username = reply.user.username,
                    content = reply.rawContent,
                    sentiment = sentiment_analyzer(reply.rawContent),
                    tweet_id = reply.inReplyToTweetId,
                    tweet_owner_id = the_account.id)
        session.add(reply_model)
        session.commit()
