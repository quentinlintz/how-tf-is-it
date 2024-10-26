from datetime import datetime

import pytz


def format_timezone(tzinfo_str):
    parts = tzinfo_str.split("/")
    if len(parts) == 2:
        return f"{parts[1].replace('_', ' ')}, {parts[0]}"
    return tzinfo_str


def create_post(timezone="America/New_York"):
    now = datetime.now(pytz.timezone(timezone))
    time_string = now.strftime("%-I:%M %p")
    area = format_timezone(timezone)
    return f"how tf is it {time_string} in {area} already?"
