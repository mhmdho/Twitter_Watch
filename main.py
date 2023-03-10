from fastapi import FastAPI, Depends
from fastapi_utils.tasks import repeat_every
from database import SessionLocal
from sqlalchemy.orm import Session
from scrapers import get_replies, get_tweets, get_accounts
import uvicorn
import models


accounts = ['@alikarimi_ak8', '@elonmusk', '@BarackObama',
            '@taylorlorenz', '@cathiedwood', '@ylecun']
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
def background_task():
  get_tweets('barackobama')
  get_replies('barackobama')


@app.get("/api/v1/accounts")
def read_api(db: Session = Depends(get_db)):
  return db.query(models.Accounts).all()


uvicorn.run(app, port = 8080, host = "0.0.0.0")
