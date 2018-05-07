from src.p03_strings.p02_string_split_and_join import string_split_and_join
from tests.test_case import TestCase


class TestStringSplitAndJoin(TestCase):
    def setUp(self):
        self.script = string_split_and_join.__file__

    def test_default_case(self):
        actual = self.execute(self.script, 'this is a string\n')

        self.assertEquals('this-is-a-string\n', actual)