import unittest

import pytz

from bot.post import create_post


class TestPost(unittest.TestCase):
    def test_create_post_default_timezone(self):
        new_post = create_post()
        print(new_post)
        self.assertIsInstance(new_post, str)
        self.assertGreater(len(new_post), 0)
        self.assertRegex(
            new_post,
            r"^how tf is it \d{1,2}:\d{2} [AP]M \([A-Z]{2,}\) already\?$"
        )

    def test_create_post_utc_timezone(self):
        new_post = create_post("UTC")
        print(new_post)
        self.assertIsInstance(new_post, str)
        self.assertGreater(len(new_post), 0)
        self.assertRegex(
            new_post, r"^how tf is it \d{1,2}:\d{2} [AP]M \(UTC\) already\?$"
        )

    def test_create_post_specific_timezone(self):
        new_post = create_post("America/Los_Angeles")
        print(new_post)
        self.assertIsInstance(new_post, str)
        self.assertGreater(len(new_post), 0)
        self.assertRegex(
            new_post,
            r"^how tf is it \d{1,2}:\d{2} [AP]M \([A-Za-z]+\) already\?$",
        )

    def test_create_post_invalid_timezone(self):
        with self.assertRaises(pytz.exceptions.UnknownTimeZoneError):
            create_post("Invalid/Timezone")


if __name__ == "__main__":
    unittest.main()

