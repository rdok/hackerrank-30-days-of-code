import unittest
import subprocess
from ddt import ddt, data, unpack

@ddt
class TestLists(unittest.TestCase):

    def setUp(self):
        self.process = subprocess.Popen(["python", "lists.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)

    def tearDown(self):
        self.process = None

    def test_zero_commands(self):
        actualOuput = self.process.communicate( input = '0\n' )[0]
        self.assertEquals('', actualOuput); 

    def test_one_command(self):
        actualOuput = self.process.communicate( input = '1\nprint\n' )[0]
        self.assertEquals('[]\n', actualOuput); 

    def test_two_commands(self):
        actualOuput = self.process.communicate( input = '2\ninsert 0 5\nprint\n' )[0]
        self.assertEquals('[5]\n', actualOuput); 

if __name__ == '__main__':
    unittest.main()
