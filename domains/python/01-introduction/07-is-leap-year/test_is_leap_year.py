import unittest
import is_leap_year
import subprocess
from ddt import ddt, data, unpack

@ddt
class TestLeapYear(unittest.TestCase):

    def test_is_evenly_dived(self):
        self.assertTrue(is_leap_year.check(2000)); 
        self.assertTrue(is_leap_year.check(1992)); 
        self.assertTrue(is_leap_year.check(1904)); 
        self.assertFalse(is_leap_year.check(1901)); 
        self.assertFalse(is_leap_year.check(1900)); 
        self.assertTrue(is_leap_year.check(2400)); 

    def test_is_evenly_dived_by_4(self):
        self.assertTrue(is_leap_year.divableByFour(2000)); # divided by all
        self.assertTrue(is_leap_year.divableByFour(1904)); # not divided by 100 or 400

    def test_is_not_evenly_divided_by_4(self):
        self.assertFalse(is_leap_year.divableByFour(1901));

    def test_is_evenly_dived_by_100(self):
        self.assertTrue(is_leap_year.divableByHundred(2000)); # divided by 4, 100, and 400
        self.assertTrue(is_leap_year.divableByHundred(1900)); # not divided by 400

    def test_is_not_evenly_divided_by_100_but_divided_by_400(self):
        self.assertFalse(is_leap_year.divableByHundred(1901));

    def test_is_evenly_dived_by_400(self):
        self.assertTrue(is_leap_year.divableByFourHundred(2400));

    def test_is_not_evenly_dived_by_400(self):
        self.assertFalse(is_leap_year.divableByFourHundred(2500));

    def test_prints_expected_outpout(self):
        self.process = subprocess.Popen(["python", "is_leap_year.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
        actualOuput = self.process.communicate( input = '1990' )[0]
        self.assertEquals( 'False\n', actualOuput )

if __name__ == '__main__':
    unittest.main()
