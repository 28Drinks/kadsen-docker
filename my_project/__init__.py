from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from sqlalchemy_utils import create_database, database_exists
from apscheduler.schedulers.background import BackgroundScheduler
# from flask_alembic import Alembic

app = Flask(__name__)

sched = BackgroundScheduler(daemon = True)
sched.start()

# app.config.from_pyfile("config.py")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pls_db.db"

# app.config["SECRET_KEY"] = ""

# alembic = Alembic()
# alembic.init_app(app)

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from my_project import routes

from my_project.models import Lotto,Winner,Staker,Jackpot,currentJackpot, currentLotto , SportsBots, User, SportBot
# db.drop_all() #don't do this!
db.create_all()
db.session.commit()
# db.init_app(app)
# with app.app_context():
#     db.create_all()
#     db.session.commit()


import get_share_values

# @sched.scheduled_job(trigger = 'cron', minute = 36, hour = 20)
# def get_values():
#     get_share_values.main()