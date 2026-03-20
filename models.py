"""Map database models in sqlalchemy for the flask app"""
import datetime
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, String, Date
#import pdb

load_dotenv()  # load variables from .env or with pathlib?

app = Flask(__name__)
# connection string constructor
# driver is psycopg # python adapter psycopg
# flask configutarion variable to tell the app which db should connect
# dialect+driver://username:password@host:port/database # db dialect
## /// ## is a relative file path
#pdb.set_trace()
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql+psycopg://{os.getenv('SUPABASE_DB_USER')}:"
    f"{os.getenv('SUPABASE_DB_PASSWORD')}@"
    f"{os.getenv('SUPABASE_DB_HOST')}:"
    f"{os.getenv('SUPABASE_DB_PORT')}/"
    f"{os.getenv('SUPABASE_DB_NAME')}"
)
# flask sqlalchemy event notification system that gets layered on top of sqlalachemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # do not track object modifications. slows down the app. even tho not importing models_commited

db = SQLAlchemy(app)


class Project(db.Model):
    """SQLAlchemy model"""
    __tablename__ = 'projects'
    # primary_key is implicitly nullable=False
    id: Mapped[int] = mapped_column(primary_key=True) # missing user ownership
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    created: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    skills: Mapped[str] = mapped_column(Text, nullable=False)
    github_repo: Mapped[str] = mapped_column(Text, unique=True, nullable=False)

    def __repr__(self):
        return f'''<Project (Title: {self.title}
                Description: {self.description}
                Skills: {self.skills}
                Github: {self.github_repo})'''