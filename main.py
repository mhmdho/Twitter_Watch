from fastapi import FastAPI, Depends
from fastapi_utils.tasks import repeat_every
from database import SessionLocal
from sqlalchemy.orm import Session
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
def tweets_task():
  for item in accounts:
    get_tweets(item)
    # get_replies(item)



@app.get("/api/v1/accounts")
def accounts_api(db: Session = Depends(get_db)):
  return db.query(models.Accounts).all()

@app.get("/api/v1/{account}/tweets")
def tweets_api(account: str, db: Session = Depends(get_db)):
  the_account = db.query(models.Accounts).filter(
                  models.Accounts.username == account.lower()).first()
  return the_account.actweets


uvicorn.run(app, port = 8080, host = "0.0.0.0")
