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

        self.assertEquals(
            """
------------.|.------------\n
---------.|..|..|.---------\n
------.|..|..|..|..|.------\n
---.|..|..|..|..|..|..|.---\n
----------WELCOME----------\n
---.|..|..|..|..|..|..|.---\n
------.|..|..|..|..|.------\n
---------.|..|..|.---------\n
------------.|.------------\n
            """,
            actual_output
        )


if __name__ == '__main__':
    unittest.main()
