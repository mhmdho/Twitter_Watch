from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base, engine


class Accounts(Base):
  __tablename__ = "Accounts"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  sentiment = Column(Float)
  name = Column(String)
  description = Column(String)
  verified = Column(Boolean)
  created_at = Column(DateTime)
  followers_count = Column(Integer)
  friends_count = Column(Integer)
  location = Column(String)
  image = Column(String)
  tweets_count = Column(Integer)
  weblink = Column(String)
  label_desc = Column(String)
  label_url = Column(String)
  summary_desc = Column(String)
  

  actweets = relationship("Tweets", back_populates="tweetowner")
  acreplies = relationship("Replies", back_populates="rptwowner")


class Tweets(Base):
  __tablename__ = "Tweets"

  id = Column(Integer, primary_key=True, index=True)
  date = Column(DateTime)
  username = Column(String)
  content = Column(String)
  sentiment = Column(Float)
  owner_id = Column(Integer, ForeignKey("Accounts.id"))

  tweetowner = relationship("Accounts", back_populates="actweets")


class Replies(Base):
  __tablename__ = "Relplies"

  id = Column(Integer, primary_key=True, index=True)
  date = Column(DateTime)
  username = Column(String)
  content = Column(String)
  sentiment = Column(Float)
  tweet_id = Column(Integer, ForeignKey("Tweets.id"))
  tweet_owner_id = Column(Integer, ForeignKey("Accounts.id"))

  rptwowner = relationship("Accounts", back_populates="acreplies")


Base.metadata.create_all(bind=engine)
