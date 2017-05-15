import unittest
import subprocess

class TestTextAlignment(unittest.TestCase):

    def setUp(self):
        self.process = subprocess.Popen( 
            ["python", "text_alignment.py"],
            stdout=subprocess.PIPE, stdin=subprocess.PIPE, 
            stderr=subprocess.STDOUT 
        )

    def tearDown(self):
        self.process = None

    def test_default_case(self):
        actual_output = self.process.communicate( input = '5\n' )[0]
        self.assertEquals("H           HHH            HHHHH            HHHHHHH           HHHHHHHHH            HHHHH               HHHHH                           HHHHH               HHHHH                             HHHHH               HHHHH                               HHHHH               HHHHH                                 HHHHH               HHHHH                                   HHHHH               HHHHH                                     HHHHHHHHHHHHHHHHHHHHHHHHH                             HHHHHHHHHHHHHHHHHHHHHHHHH                               HHHHHHHHHHHHHHHHHHHHHHHHH                                 HHHHH               HHHHH                                             HHHHH               HHHHH                                               HHHHH               HHHHH                                                 HHHHH               HHHHH                                                   HHHHH               HHHHH                                                     HHHHH               HHHHH                                                                         HHHHHHHHH                                                                                  HHHHHHH                                                                                                         HHHHH                                                                                                                                 HHH                                                                                                                                                          H                 ' != '    H    \n   HHH   \n  HHHHH  \n HHHHHHH \nHHHHHHHHH\n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHHHHHHHHHHHHHHHHHHHHHH   \n  HHHHHHHHHHHHHHHHHHHHHHHHH   \n  HHHHHHHHHHHHHHHHHHHHHHHHH   \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n                    HHHHHHHHH \n                     HHHHHHH  \n                      HHHHH   \n                       HHH    \n                        H     \n", actual_output ); 

if __name__ == '__main__':
    unittest.main()
