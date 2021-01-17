from unittest import TestCase
from cpu_info import get_cpu_info


class CpuInfoTest(TestCase):
    def setUp(self):
        self.content = get_cpu_info()

    def test_get_cpu_info(self):
        self.assertTrue(self.content)

    def test_cpu_info_content(self):
        """CPU Info content dict must contain expected keys"""
        expected = ["cpu_brand", "cpu_count", "cpu_freq"]
        with self.subTest():
            for key in expected:
                self.assertIn(key, self.content)