from unittest import TestCase, main
import doctest
from lessons import divisor
def load_tests(loader,tests,ignore):
    tests.addTests(doctest.DocTestSuite(divisor)) # дополняет тесты - doctest из divisor
    return tests
class TestDivisor(TestCase):
    def test_zero_raises(self):
        with self.assertRaises(ValueError):
            divisor.divide(10,0)
if __name__=='__main__':
    main()