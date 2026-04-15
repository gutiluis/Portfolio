#!/bin/env python


"""
Database sqlalchemy model mapper
"""

import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, String, Date

from . import db  # import extension not app

"""
Flask sqlalchemy event notification system
that gets layered on top of sqlalachemy
"""


class Project(db.Model):
    """SQLAlchemy table model and db schema definition"""

    __tablename__ = "projects"
    # primary_key is implicitly nullable=False
    # missing user ownership for db policies
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    created: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    skills: Mapped[str] = mapped_column(Text, nullable=False)
    github_repo: Mapped[str] = mapped_column(Text, unique=True, nullable=False)

    def __repr__(self):
        return f"""<Project (Title: {self.title}
                Description: {self.description}
                Skills: {self.skills}
                Github: {self.github_repo})"""
