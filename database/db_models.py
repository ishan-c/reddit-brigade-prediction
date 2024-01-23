from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

Base = declarative_base()


class Submission(Base):
    __tablename__ = "submissions"
    submission_id = Column(String, primary_key=True)
    subreddit_id = Column(String)
    author_name = Column(String)
    score = Column(Integer)
    post_time = Column(DateTime)
    retrieved = Column(DateTime)
    num_comments = Column(Integer)
    title = Column(String)
    is_self = Column(Boolean)
    body = Column(String)
    edited = Column(DateTime)
    domain = Column(String)
    full_url = Column(String)
    locked = Column(Boolean)
    stickied = Column(Boolean)
    gilded = Column(Integer)
    over_18 = Column(Boolean)


class Comment(Base):
    __tablename__ = "comments"
    comment_id = Column(String, primary_key=True)
    parent_id = Column(String)
    submission_id = Column(String)
    subreddit_id = Column(String)
    author_name = Column(String)
    score = Column(Integer)
    controversiality = Column(Boolean)
    post_time = Column(DateTime)
    retrieved = Column(DateTime)
    body = Column(String)
    edited = Column(DateTime)
    stickied = Column(Boolean)
    gilded = Column(Integer)


class Subreddit(Base):
    __tablename__ = "subreddits"
    subreddit_id = Column(String, primary_key=True)
    subreddit_name = Column(String)
