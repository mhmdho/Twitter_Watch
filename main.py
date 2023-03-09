from fastapi import FastAPI, Depends
from fastapi_utils.tasks import repeat_every
from database import SessionLocal
from sqlalchemy.orm import Session
from scrapers import get_replies, get_tweets
import uvicorn
import models


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
  # get_replies('barackobama')


@app.get("/")
def read_api(db: Session = Depends(get_db)):
  return db.query(models.Replies).all()


uvicorn.run(app, port = 8080, host = "0.0.0.0")
