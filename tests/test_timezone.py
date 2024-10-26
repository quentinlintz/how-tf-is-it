import unittest
from datetime import datetime
from unittest.mock import patch

import pytz

from bot.timezone import get_timezone


class TestTimezone(unittest.TestCase):
    @patch("bot.timezone.datetime")
    def test_get_timezone_afternoon(self, mock_datetime):
        fixed_time = datetime(2023, 10, 26, 15, 0, 0, tzinfo=pytz.utc)
        mock_datetime.now.return_value = fixed_time

        timezone = get_timezone()

        self.assertIsNotNone(timezone)

    @patch("bot.timezone.datetime")
    def test_get_timezone_morning(self, mock_datetime):
        fixed_time = datetime(2023, 10, 26, 8, 0, 0, tzinfo=pytz.utc)
        mock_datetime.now.return_value = fixed_time

        timezone = get_timezone()

        self.assertEqual(timezone, "America/New_York")


if __name__ == "__main__":
    unittest.main()
