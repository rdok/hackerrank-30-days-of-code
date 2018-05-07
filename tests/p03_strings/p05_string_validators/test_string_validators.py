from src.p03_strings.p05_string_validators import string_validators
from tests.test_case import TestCase


class TestStringValidators(TestCase):
    def setUp(self):
        self.script =  string_validators.__file__

    def test_default_case(self):
        actual = self.execute(self.script, 'qA2\n')
        self.assertEquals('True\nTrue\nTrue\nTrue\nTrue\n', actual)

    def test_only_alphabetical(self):
        actual = self.execute(self.script, 'qA\n')
        self.assertEquals('True\nTrue\nFalse\nTrue\nTrue\n', actual)

    def test_only_digit(self):
        actual = self.execute(self.script, '134\n')
        self.assertEquals('True\nFalse\nTrue\nFalse\nFalse\n', actual)

    def test_only_lower(self):
        actual = self.execute(self.script, 'lower\n')
        self.assertEquals('True\nTrue\nFalse\nTrue\nFalse\n', actual)

    def test_only_upper(self):
        actual = self.execute(self.script, 'UPPER\n')
        self.assertEquals('True\nTrue\nFalse\nFalse\nTrue\n', actual)