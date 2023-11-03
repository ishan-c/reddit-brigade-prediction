from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String

Base = declarative_base()


class Submission(Base):
    """Collects information from a submission entry

    Attributes:
            id (int): Primary key, the submission id from Reddit
    """

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
    gilded = Column(Boolean)
    over_18 = Column(Boolean)

    __table_args__ = (
        UniqueConstraint('subreddit_id', 'author_name', 'post_time'),
    )


class Comment(Base):
    """Collects information from a comment entry

        Attributes:
            id (int): Primary key, the comment id from Reddit
    """
    __tablename__ = "comments"
    comment_id = Column(String, primary_key=True)
    parent_id = Column(String)
    submission_id = Column(String, ForeignKey('submissions'))
    author_name = Column(String)
    score = Column(Integer)
    controversiality = Column(Boolean)
    post_time = Column(DateTime)
    retrieved = Column(DateTime)
    body = Column(String)
    edited = Column(DateTime)
    stickied = Column(Boolean)
    gilded = Column(Boolean)

    __table_args__ = (
        UniqueConstraint('parent_id', 'author_name', 'post_time'),
    )


class Subreddit(Base):
    """Stores information at a subreddit level

        Attributes:
            id (int): Primary key, the subreddit id from Reddit
    """
    __tablename__ = "subreddits"
    subreddit_id = Column(String, primary_key=True)
    subreddit_name = Column(String)

    __table_args__ = (
        UniqueConstraint('subreddit_name'),
    )
