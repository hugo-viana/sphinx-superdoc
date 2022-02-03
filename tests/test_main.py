from unittest import TestCase

from sphinx_superdoc.main import console


class Test_Main(TestCase):

    def test_console(self):
        """Ensure console success return code."""
        retcode = console()  # act

        self.assertEqual(retcode, 0)
