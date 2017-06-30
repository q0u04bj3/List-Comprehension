import unittest
from ListComprehension import fun

class ListComprehensionTest(unittest.TestCase):
    
    def test_ListComprehension_zero(self):
        expected_value = 0
        value = fun(0,0)
        self.assertEqual(expected_value, value)
    
    def test_ListComprehension_num1(self):
        expected_value = -55
        value = fun(1,11)
        self.assertEqual(expected_value, value)
    
    def test_ListComprehension_num1(self):
        expected_value = 4951
        value = fun(1,20)
        self.assertEqual(expected_value, value)

    def test_ListComprehension_num2(self):
        expected_value = 0
        value = fun(10,10)
        self.assertEqual(expected_value, value)

    def test_ListComprehension_num3(self):
        expected_value = 0
        value = fun(-1,100)
        self.assertEqual(expected_value, value)

    def test_ListComprehension_num4(self):
        expected_value = 0
        value = fun(-1,-100)
        self.assertEqual(expected_value, value)


if __name__ == '__main__':
    unittest.main()
