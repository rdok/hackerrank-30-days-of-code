import unittest
from ddt import ddt, data, unpack
import subprocess

@ddt
class TestLists(unittest.TestCase):

    def test_greeting(self):
        process = subprocess.Popen(["python", "lists.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
        actualOuput = process.communicate(
                input = '12\ninsert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove 6\nappend 9\nappend 1\nsort\nprint\npop\nreverse\nprint'
        )[0]
        self.assertEquals('[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]\n', actualOuput); 

if __name__ == '__main__':
    unittest.main()
