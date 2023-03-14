# Twitter Watch

This project tracks tweets and replies of six following accounts from **February 1st, 2023** and keep running and update information:
- @alikarimi_ak8
- @elonmusk
- @BarackObama
- @taylorlorenz
- @cathiedwood
- @ylecun

Then for each account process and extracts some information based on the tracked data as the following :

- All tweets that each include data such as name of the author, time of the tweet and
text of the tweet.
- Active audiences which reply to tweets of the account.
- Sentiment scores to each of the following:
    - How positive or negative each Tweet is.
    - How positive or negative audience (reply) of each thread is.
- Summary description of each account by the Use of AI


**ERD**:
-
In the next step, ERD of the database designed and the data stored in the database.
![ERD0_Tw](https://user-images.githubusercontent.com/90003763/225167435-a3ef254b-d4b2-472c-960e-a8859498abee.png)



**Technologies**:
-
- Python
- FastAPI
- SQLalchemy (database)
- Swagger
- JQuery
- HTML
- CSS



**API Endpoints Information:**
-
- /accounts: a json list of all tracked accounts.
- /tweets/< account >: a json of the user's tweets since start.
- /replies/< account >: a json of the user's replies since start.
- /audience/< account > : return a json of information about the audience for a user's account.
- /sentiment/< account > : a json of information about the sentiment level of tweet and audience for an account.
- /accounts/sentiment: a json of total sentiment level for all accounts.


In addition, the front website is designed and the all the above data is shown on it for each account
