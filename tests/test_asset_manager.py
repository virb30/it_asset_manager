from unittest import TestCase
from asset_manager import get_asset_info


class AssetManagerTest(TestCase):
    def setUp(self):
        self.content = get_asset_info()

    def test_get_asset_info(self):
        self.assertTrue(self.content)

    def test_asset_info_content(self):
        """Asset info must contain keys"""
        expected = ["system_info", "cpu_info", "disk_info"]

        with self.subTest():
            for key in expected:
                self.assertIn(key, self.content)