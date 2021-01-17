from unittest import TestCase
from system_info import get_system_info


class SystemInfoTest(TestCase):
    def setUp(self):
        self.content = get_system_info()

    def test_get_system_info(self):
        self.assertTrue(self.content)

    def test_system_info_content(self):
        """System Info content dict must contain expected keys"""
        expected = ["arch", "system", "build", "name"]

        with self.subTest():
            for key in expected:
                self.assertIn(key, self.content)
