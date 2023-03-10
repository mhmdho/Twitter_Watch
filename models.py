from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine


class Accounts(Base):
  __tablename__ = "Accounts"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  description = Column(String)

  actweets = relationship("Tweets", back_populates="owner_id")


class Tweets(Base):
  __tablename__ = "Tweets"

  id = Column(Integer, primary_key=True, index=True)
  date = Column(DateTime)
  username = Column(String)
  content = Column(String)
  owner_id = Column(Integer, ForeignKey("Accounts.id"))



class Replies(Base):
  __tablename__ = "Relplies"

  id = Column(Integer, primary_key=True, index=True)
  date = Column(DateTime)
  username = Column(String)
  content = Column(String)


Base.metadata.create_all(bind=engine)
