import os
import subprocess
import unittest

from ddt import ddt


@ddt
class TestLists(unittest.TestCase):
    def test_zero_commands(self):
        actual_output = self.execute_script('0\n')
        self.assertEquals('', actual_output)

    def test_two_commands(self):
        actual_output = self.execute_script('2\ninsert 0 5\nprint\n')
        self.assertEquals('[5]\n', actual_output)

    def test_print(self):
        actual_output = self.execute_script('2\ninsert 0 5\nprint\n')
        self.assertEquals('[5]\n', actual_output)

    def test_insert(self):
        actual_output = self.execute_script('2\ninsert 0 5\nprint\n')
        self.assertEquals('[5]\n', actual_output)

    def test_remove(self):
        actual_output = self.execute_script(
            '4\ninsert 0 5\ninsert 1 10\nremove 5\nprint\n'
        )
        self.assertEquals('[10]\n', actual_output)

    def test_append(self):
        actual_output = self.execute_script('2\nappend 10\nprint\n')
        self.assertEquals('[10]\n', actual_output)

    def test_sort(self):
        actual_output = self.execute_script('3\nappend 10\nappend 5\nprint\n')
        self.assertEquals('[10, 5]\n', actual_output)

        actual_output = self.execute_script(
            '4\nappend 10\nappend 5\nsort\nprint\n'
        )

        self.assertEquals('[5, 10]\n', actual_output)

    def test_pop(self):
        actual_output = self.execute_script('3\nappend 10\npop\nprint\n')

        self.assertEquals('[]\n', actual_output)

    def test_reverse(self):
        actual_output = self.execute_script(
            '4\nappend 10\nappend 5\nreverse\nprint\n'
        )

        self.assertEquals('[5, 10]\n', actual_output)

    def test_case_1(self):
        actual_output = self.execute_script(
            '12\ninsert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove '
            '6\nappend 9\nappend 1\nsort\nprint\npop\nreverse\nprint\n'
        )

        self.assertEquals(
            '[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]\n',
            actual_output
        )

    def execute_script(self, argument):
        script = os.path.dirname(os.path.realpath(__file__)) + "/lists.py"

        self.process = subprocess.Popen(
            ["python", script],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

        return self.process.communicate(argument)[0]


if __name__ == '__main__':
    unittest.main()
