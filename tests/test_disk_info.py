from disk_info import get_disk_info
from unittest import TestCase


class DiskInfoTest(TestCase):
    def setUp(self):
        self.content = get_disk_info()

    def test_get_disk_info(self):
        self.assertTrue(self.content)

    def test_disk_info_content(self):
        expected = ["path", "total", "used", "free", "percent"]

        with self.subTest():
            for disk in self.content:
                self.assertSequenceEqual(expected, list(disk.keys()))