import subprocess
import unittest


class TestTextWrap(unittest.TestCase):
    def setUp(self):
        self.process = subprocess.Popen(
            ["python", "designer_door_mat.py"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    def tearDown(self):
        self.process = None

    def test_first_line(self):
        actual_output = self.process.communicate(
            input='9\n27\n'
        )[0]

        self.assertEquals(
            "------------.|.------------\n",
            actual_output
        )

    def test_default_case(self):
        actual_output = self.process.communicate(
            input='9\n27\n'
        )[0]

        self.assertEquals(
            "------------.|.------------\n"
            "---------.|..|..|.---------\n"
            "------.|..|..|..|..|.------\n"
            "---.|..|..|..|..|..|..|.---\n"
            "----------WELCOME----------\n"
            "---.|..|..|..|..|..|..|.---\n"
            "------.|..|..|..|..|.------\n"
            "---------.|..|..|.---------\n"
            "------------.|.------------\n",
            actual_output
        )


if __name__ == '__main__':
    unittest.main()
