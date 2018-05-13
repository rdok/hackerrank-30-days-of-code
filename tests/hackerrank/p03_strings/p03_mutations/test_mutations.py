from src.hackerrank.p03_strings.p03_mutations import mutations
from tests.test_case import TestCase


class TestMutations(TestCase):
    def setUp(self):
        self.script = mutations.__file__

    def test_default_case(self):
        actual = self.execute(self.script, 'abracadabra\n5 k\n')
        self.assertEquals('abrackdabra\n', actual)
