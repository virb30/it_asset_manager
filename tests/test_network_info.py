from unittest import TestCase
from network_info import get_network_info


class NetworkInfoTest(TestCase):
    def setUp(self):
        self.content = get_network_info()

    def test_get_network_info(self):
        self.assertTrue(self.content)

    def test_network_info_content(self):
        """Network info must be a list of dictionaries with expected keys"""
        expected = ["nice_name", "mac", "ip", "ip6"]

        self.assertIsInstance(self.content, list)

        with self.subTest():
            for interface in self.content:
                for key in expected:
                    self.assertIn(key, interface)
