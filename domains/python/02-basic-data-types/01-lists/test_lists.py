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

    def test_two_commands(self):
        actualOuput = self.process.communicate( input = '2\ninsert 0 5\nprint\n' )[0]
        self.assertEquals('[5]\n', actualOuput); 

    def test_print(self):
        actualOuput = self.process.communicate( input = '2\ninsert 0 5\nprint\n' )[0]
        self.assertEquals('[5]\n', actualOuput); 

    def test_insert(self):
        actualOuput = self.process.communicate( input = '2\ninsert 0 5\nprint\n' )[0]
        self.assertEquals('[5]\n', actualOuput); 

    def test_remove(self):
        actualOuput = self.process.communicate( input = '4\ninsert 0 5\ninsert 1 10\nremove 5\nprint\n' )[0]
        self.assertEquals('[10]\n', actualOuput); 

    def test_append(self):
        actualOuput = self.process.communicate( input = '2\nappend 10\nprint\n' )[0]
        self.assertEquals('[10]\n', actualOuput); 

    def test_sort(self):
        actualOuput = self.process.communicate( input = '3\nappend 10\nappend 5\nprint\n' )[0]
        self.assertEquals('[10, 5]\n', actualOuput); 

        process = subprocess.Popen(["python", "lists.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
        actualOuput = process.communicate( input = '4\nappend 10\nappend 5\nsort\nprint\n' )[0]
        self.assertEquals('[5, 10]\n', actualOuput); 

    def test_pop(self):
        actualOuput = self.process.communicate( input = '3\nappend 10\npop\nprint\n' )[0]
        self.assertEquals('[]\n', actualOuput); 

    def test_reverse(self):
        actualOuput = self.process.communicate( input = '4\nappend 10\nappend 5\nreverse\nprint\n' )[0]
        self.assertEquals('[5, 10]\n', actualOuput); 

    def test_case_1(self):
        actualOuput = self.process.communicate( input = '12\ninsert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove 6\nappend 9\nappend 1\nsort\nprint\npop\nreverse\nprint\n' )[0]
        self.assertEquals('[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]\n', actualOuput); 

if __name__ == '__main__':
    unittest.main()
