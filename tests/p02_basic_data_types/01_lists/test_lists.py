from src.p02_basic_data_types.p01_lists import lists

from tests.test_case import TestCase


class TestLists(TestCase):
    def setUp(self):
        self.script = lists.__file__

    def test_zero_commands(self):
        actual = self.execute(self.script, '0\n')
        self.assertEquals('', actual)

    def test_print_and_insert_commands(self):
        actual = self.execute(self.script, '2\ninsert 0 5\nprint\n')
        self.assertEquals('[5]\n', actual)

    def test_remove(self):
        user_input = '4\ninsert 0 5\ninsert 1 10\nremove 5\nprint\n'
        actual = self.execute(self.script, user_input)
        self.assertEquals('[10]\n', actual)

    def test_append(self):
        actual = self.execute(self.script, '2\nappend 10\nprint\n')
        self.assertEquals('[10]\n', actual)

    def test_sort(self):
        user_input = '4\nappend 10\nappend 5\nsort\nprint\n'
        actual = self.execute(self.script, user_input)
        self.assertEquals('[5, 10]\n', actual)

    def test_pop(self):
        user_input = '3\nappend 10\npop\nprint\n'
        actual = self.execute(self.script, user_input)
        self.assertEquals('[]\n', actual)

    def test_reverse(self):
        user_input = '4\nappend 10\nappend 5\nreverse\nprint\n'
        actual = self.execute(self.script, user_input)
        self.assertEquals('[5, 10]\n', actual)

    def test_case_1(self):
        user_input = '12\ninsert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove ' \
                     '6\nappend 9\nappend 1\nsort\nprint\npop\nreverse\nprint\n'
        actual_output = self.execute(self.script, user_input)
        expected = '[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]\n'
        self.assertEquals(expected, actual_output)
