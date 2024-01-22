from datetime import datetime


def transform_date(input_str: str) -> datetime:
    return datetime.utcfromtimestamp(int(input_str))


def transform_date_with_bool(input_str: str):
    if input_str == "False":
        return None
    return transform_date(input_str)


def transform_field(field_name, data):
    if field_name in ["created_utc", "retrieved_on"]:
        return transform_date(data)
    elif field_name == "edited":
        return transform_date_with_bool(data)
