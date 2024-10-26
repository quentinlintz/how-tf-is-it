import unittest

import pytz

from bot.post import create_post, format_timezone


class TestPost(unittest.TestCase):
    def test_format_timezone_standard(self):
        self.assertEqual(format_timezone("America/New_York"), "New York, America")
        self.assertEqual(format_timezone("Africa/Banjul"), "Banjul, Africa")
        self.assertEqual(format_timezone("Asia/Tokyo"), "Tokyo, Asia")

    def test_format_timezone_single_word(self):
        self.assertEqual(format_timezone("UTC"), "UTC")
        self.assertEqual(format_timezone("Europe"), "Europe")

    def test_format_timezone_underscore_in_city(self):
        self.assertEqual(
            format_timezone("America/Argentina_Buenos_Aires"),
            "Argentina Buenos Aires, America",
        )

    def test_create_post_default_timezone(self):
        new_post = create_post()
        print(new_post)
        self.assertIsInstance(new_post, str)
        self.assertGreater(len(new_post), 0)
        self.assertRegex(
            new_post,
            r"^how tf is it \d{1,2}:\d{2} [AP]M in [\w\s]+, [\w\s]+ already\?$",
        )

    def test_create_post_utc_timezone(self):
        new_post = create_post("UTC")
        print(new_post)
        self.assertIsInstance(new_post, str)
        self.assertGreater(len(new_post), 0)
        self.assertRegex(
            new_post, r"^how tf is it \d{1,2}:\d{2} [AP]M in UTC already\?$"
        )

    def test_create_post_specific_timezone(self):
        new_post = create_post("America/Los_Angeles")
        print(new_post)
        self.assertIsInstance(new_post, str)
        self.assertGreater(len(new_post), 0)
        self.assertRegex(
            new_post,
            r"^how tf is it \d{1,2}:\d{2} [AP]M in Los Angeles, America already\?$",
        )

    def test_create_post_invalid_timezone(self):
        with self.assertRaises(pytz.exceptions.UnknownTimeZoneError):
            create_post("Invalid/Timezone")


if __name__ == "__main__":
    unittest.main()
