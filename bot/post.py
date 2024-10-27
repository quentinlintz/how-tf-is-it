from datetime import datetime

import pytz


def create_post(timezone="America/New_York"):
    now = datetime.now(pytz.timezone(timezone))
    time_string = now.strftime("%-I:%M %p")
    return f"how tf is it {time_string} ({now.tzname()}) already?"
