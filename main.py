from fastapi import FastAPI, Depends
from fastapi_utils.tasks import repeat_every
from database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import func
from scrapers import get_replies, get_tweets, get_accounts
import uvicorn
import models


accounts = ['alikarimi_ak8', 'elonmusk', 'BarackObama',
            'taylorlorenz', 'cathiedwood', 'ylecun']
get_accounts(accounts)


app = FastAPI()


def get_db():
  try:
    db = SessionLocal()
    yield db
  finally:
    db.close()



@app.on_event("startup")
@repeat_every(seconds=10)
def tweets_task0():
    get_tweets(accounts[0])
    get_replies(accounts[0])

@app.on_event("startup")
@repeat_every(seconds=11)
def tweets_task1():
    get_tweets(accounts[1])
    get_replies(accounts[1])

@app.on_event("startup")
@repeat_every(seconds=12)
def tweets_task2():
    get_tweets(accounts[2])
    get_replies(accounts[2])

@app.on_event("startup")
@repeat_every(seconds=13)
def tweets_task3():
    get_tweets(accounts[3])
    get_replies(accounts[3])

@app.on_event("startup")
@repeat_every(seconds=14)
def tweets_task4():
    get_tweets(accounts[4])
    get_replies(accounts[4])

@app.on_event("startup")
@repeat_every(seconds=15)
def tweets_task5():
    get_tweets(accounts[5])
    get_replies(accounts[5])




@app.get("/api/v1/accounts")
def accounts_api(db: Session = Depends(get_db)):
  return db.query(models.Accounts).all()

@app.get("/api/v1/{account}/tweets")
def tweets_api(account: str, db: Session = Depends(get_db)):
  the_account = db.query(models.Accounts).filter(
                  models.Accounts.username == account.lower()).first()
  return the_account.actweets

@app.get("/api/v1/{account}/replies")
def replies_api(account: str, db: Session = Depends(get_db)):
  the_account = db.query(models.Accounts).filter(
                  models.Accounts.username == account.lower()).first()
  return the_account.acreplies

@app.get("/api/v1/{account}/audience")
def audience_api(account: str, db: Session = Depends(get_db)):
  the_account = (db.query(models.Accounts)
                   .filter(models.Accounts.username == account.lower())
                   .first())
  audience = (db.query(models.Replies.username, func.count(models.Replies.username))
               .having(models.Replies.tweet_owner_id == the_account.id)
               .group_by(models.Replies.username)
               .order_by(func.count(models.Replies.username).desc()))
  min_replies = min(dict(audience.limit(10)).values())
  result = audience.having(func.count(models.Replies.username) >= min_replies)
  return result


uvicorn.run(app, port = 8080, host = "0.0.0.0")
