import unittest
from ddt import ddt, data, unpack
import subprocess

@ddt
class TestWhatsYourName(unittest.TestCase):

    def test_greeting(self):
        process = subprocess.Popen(["python", "whats_your_name.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
        actualOuput = process.communicate( input = 'James\nPotter\n' )[0]
        self.assertEquals('Hello James Potter! You just delved into python.\n', actualOuput); 

if __name__ == '__main__':
    unittest.main()
