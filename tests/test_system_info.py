from typing import Mapping
from unittest import TestCase
from get_system_info import get_system_info


class SystemInfoTest(TestCase):
    def setUp(self):
        self.content = get_system_info()

    def test_get_system_info(self):
        self.assertTrue(self.content)

    def test_system_info_content(self):
        expected = ["arch", "system", "build", "name"]

        with self.subTest():
            for key in expected:
                self.assertDictHasKey(self.content, key)

    def assertDictHasKey(self, dict_: Mapping, key):
        self.assertTrue(key in dict_.keys())
