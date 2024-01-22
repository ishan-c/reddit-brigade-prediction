from database.db_models import Comment, Submission, Subreddit

submission_map = {
    "id": "submission_id",
    "subreddit_id": "subreddit_id",
    "author": "author_name",
    "score": "score",
    "created_utc": "post_time",
    "retrieved_on": "retrieved",
    "num_comments": "num_comments",
    "title": "title",
    "is_self": "is_self",
    "selftext": "body",
    "edited": "edited",
    "domain": "domain",
    "url": "full_url",
    "locked": "locked",
    "stickied": "stickied",
    "gilded": "gilded",
    "over_18": "over_18"
}

comment_map = {
    "id": "comment_id",
    "parent_id": "parent_id",
    "link_id": "submission_id",
    "subreddit_id": "subreddit_id",
    "author": "author_name",
    "score": "score",
    "controversiality": "controversiality",
    "created_utc": "post_time",
    "retrieved_on": "retrieved",
    "body": "body",
    "edited": "edited",
    "stickied": "stickied",
    "gilded": "gilded"
}

subreddit_map = {
    "subreddit_id": "subreddit_id",
    "subreddit": "subreddit_name"
}

json_model_map = {
    Comment: comment_map,
    Submission: submission_map,
    Subreddit: subreddit_map
}
