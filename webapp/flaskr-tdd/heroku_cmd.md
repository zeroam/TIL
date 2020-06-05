## COMMAND
```bash
# login heroku
heroku login

# create app
heroku create

# add git repository
git remote add heroku <git-url>

# deploy
git push heroku master

# postgres
heroku addons:create heroku-postgresql:hobby-dev

# initialize db
heroku run python create_db.py
```