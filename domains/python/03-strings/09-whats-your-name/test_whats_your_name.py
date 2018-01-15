import os
import subprocess
import unittest

from ddt import ddt


@ddt
class TestWhatsYourName(unittest.TestCase):
    def test_greeting(self):
        script = os.path.dirname(
            os.path.realpath(__file__)) + "/whats_your_name.py"

        process = subprocess.Popen(["python", script],
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        actualOuput = process.communicate(input='James\nPotter\n')[0]
        self.assertEquals('Hello James Potter! You just delved into python.\n',
                          actualOuput);


if __name__ == '__main__':
    unittest.main()
