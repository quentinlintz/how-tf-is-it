import random
from datetime import datetime

import pytz

# A set of common timezone abbreviations
VALID_TZ_ABBREVIATIONS = {
    "UTC",
    "GMT",
    "EST",
    "EDT",
    "CST",
    "CDT",
    "MST",
    "MDT",
    "PST",
    "PDT",
    "AST",
    "ADT",
    "HST",
    "AKST",
    "AKDT",
    "NST",
    "NDT",
    "IST",
    "CET",
    "CEST",
    "EET",
    "EEST",
}


def get_timezone():
    timezones = pytz.all_timezones
    valid_timezones = []

    # Check if the current time is between 2 PM and 11 PM in each timezone
    for tz in timezones:
        local_time = datetime.now(pytz.timezone(tz))
        if 14 <= local_time.hour <= 22:
            if local_time.tzname() in VALID_TZ_ABBREVIATIONS:
                valid_timezones.append(tz)

    return random.choice(valid_timezones) if valid_timezones else "America/New_York"
