import os
import subprocess
import unittest


class TestTextWrap(unittest.TestCase):
    def setUp(self):
        script = os.path.dirname(
            os.path.realpath(__file__)) + "/designer_door_mat.py"

        self.process = subprocess.Popen(
            ["python", script],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None

    def test_default_case(self):
        actual_output = self.process.communicate('9 27\n')[0]

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
        actual_output = self.process.communicate('7 21\n')[0]

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
        actual_output = self.process.communicate('11 33\n')[0]

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

if __name__ == '__main__':
    unittest.main()
