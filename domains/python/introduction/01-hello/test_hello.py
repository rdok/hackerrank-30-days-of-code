import unittest
import subprocess

class TestStringMethods(unittest.TestCase):

    def test_see_expected_string(self):
        process = subprocess.Popen(["python", "hello.py"], stdout=subprocess.PIPE)
        actualOutput = process.communicate()[0]
        self.assertEqual('Hello, World!\n', actualOutput)

if __name__ == '__main__':
    # subprocess.Popen(["clear"])
    unittest.main()
