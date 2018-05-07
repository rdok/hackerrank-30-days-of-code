from src.p03_strings.p08_designer_door_mat import designer_door_mat
from tests.test_case import TestCase


class TestTextWrap(TestCase):
    def setUp(self):
        self.script = designer_door_mat.__file__

    def test_default_case(self):
        actual_output = self.execute(self.script, '9 27\n')
        expected_string = '------------.|.------------\n'
        self.assertTrue(
            actual_output.startswith(expected_string),
            "Expected \n%s\n not found in \n%s."
            % (expected_string, actual_output)
        )

        expected_string += '---------.|..|..|.---------\n'
        self.assertTrue(
            actual_output.startswith(expected_string),
            "Expected \n%s\n not found in \n%s."
            % (expected_string, actual_output)
        )

        expected_string += '------.|..|..|..|..|.------\n'
        self.assertTrue(
            actual_output.startswith(expected_string),
            "Expected \n%s\n not found in \n%s."
            % (expected_string, actual_output)
        )

        expected_string += '---.|..|..|..|..|..|..|.---\n'
        self.assertTrue(
            actual_output.startswith(expected_string),
            "Expected \n%s\n not found in \n%s."
            % (expected_string, actual_output)
        )

        expected_string += '----------WELCOME----------\n'
        self.assertTrue(
            actual_output.startswith(expected_string),
            "Expected \n%s\n not found in \n%s."
            % (expected_string, actual_output)
        )

        expected_string += '---.|..|..|..|..|..|..|.---\n'
        self.assertTrue(
            actual_output.startswith(expected_string),
            "Expected \n%s\n not found in \n%s."
            % (expected_string, actual_output)
        )

        expected_string += '------.|..|..|..|..|.------\n'
        self.assertTrue(
            actual_output.startswith(expected_string),
            "Expected \n%s\n not found in \n%s."
            % (expected_string, actual_output)
        )

        expected_string += '---------.|..|..|.---------\n'
        self.assertTrue(
            actual_output.startswith(expected_string),
            "Expected \n%s\n not found in \n%s."
            % (expected_string, actual_output)
        )

        expected_string += '------------.|.------------\n'
        self.assertTrue(
            actual_output.startswith(expected_string),
            "Expected \n%s\n not found in \n%s."
            % (expected_string, actual_output)
        )

        self.assertEquals(
            """------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------\n""",
            actual_output
        )

    def test_small_case(self):
        actual_output = self.execute(self.script, '7 21\n')

        self.assertEquals(
            """---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------\n""",
            actual_output
        )

    def test_big_case(self):
        actual_output = self.execute(self.script, '11 33\n')

        self.assertEquals(
            """---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------\n""",
            actual_output
        )
