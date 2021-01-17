from unittest import TestCase
from memory_info import get_memory_info


class MemoryInfoTest(TestCase):
    def setUp(self):
        self.content = get_memory_info()

    def test_get_memory_info(self):
        self.assertTrue(self.content)

    def test_memory_info_content(self):
        """Memory Info content dict must contain expected keys"""
        expected = ["total"]

        with self.subTest():
            for key in expected:
                self.assertIn(key, self.content)