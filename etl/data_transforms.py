from datetime import datetime


def transform_id(input_str: str) :
    if input_str:
        return input_str.split("_")[1]
    return None


def transform_date(input_str: str) -> datetime:
    return datetime.utcfromtimestamp(int(input_str))


def transform_date_with_bool(input_str: str):
    if input_str == "False":
        return None
    return transform_date(input_str)


def transform_field(field_name, data):
    if field_name in ["parent_id", "link_id", "subreddit_id"]:
        return transform_id(data)
    elif field_name in ["created_utc", "retrieved_on"]:
        return transform_date(data)
    elif field_name == "edited":
        return transform_date_with_bool(data)
