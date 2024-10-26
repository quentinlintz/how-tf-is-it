import random
from datetime import datetime

import pytz


def get_timezone():
    timezones = pytz.all_timezones
    valid_timezones = []

    # Check if the current time is between 2 PM and 11 PM in each timezone
    for tz in timezones:
        local_time = datetime.now(pytz.timezone(tz))
        if 14 <= local_time.hour <= 22:
            valid_timezones.append(tz)

    valid_timezones = [tz for tz in valid_timezones if tz.count("/") <= 1]

    return random.choice(valid_timezones) if valid_timezones else "America/New_York"
