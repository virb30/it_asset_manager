from unittest import TestCase
from software_info import get_installed_apps


class SoftwareInfoTest(TestCase):
    def setUp(self):
        self.content = get_installed_apps()

    def test_get_software_info(self):
        self.assertTrue(self.content)

    def test_software_info_content(self):
        """Software Info content dict must contain expected keys"""
        expected = [
            "name",
            "version",
            "install_date",
            "install_location",
            "install_source",
            "modify_path",
            "publisher",
            "uninstall_string",
        ]

        with self.subTest():
            for app in self.content:
                self.assertSequenceEqual(expected, list(app.__dict__.keys()))
