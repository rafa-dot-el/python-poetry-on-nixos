#!/usr/bin/env python3

from unittest import TestCase


class TestExampleNixTest(TestCase):
    def test_can_import_something_with_native_deps(self):
        try:
            import nix_poetry_example as example

            self.assertTrue(True)
        except Exception as e:
            self.assertEqual(str(e), "", "Expected to load library but got " + str(e))
