from src.p01_introduction.p01_hello import hello
from tests.test_case import TestCase


class TestStringMethods(TestCase):

    def setUp(self):
        self.script = hello.__file__

    def test_it_returns_hello_world_string(self):
        actual_output = self.execute(self.script)

        self.assertEqual('Hello, World!\n', actual_output)
