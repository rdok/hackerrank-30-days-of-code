from src.codeacademy.learn_python.p01_python_syntax import p01_hello_world
from tests.test_case import TestCase


class HelloWorldTest(TestCase):

    def setUp(self):
        self.script = p01_hello_world.__file__

    def test_it_prints_hello_world_string(self):
        actual_output = self.execute(self.script)

        expected = "Hello, world!\n"
        expected += "Water-there is not a drop of water there! Were Niagara "
        expected += "but a cataract of sand, would you travel your thousand miles to see it?\n"

        self.assertEqual(expected, actual_output)
