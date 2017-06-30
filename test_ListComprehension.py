import unittest
from ListComprehension import fun

class ListComprehensionTest(unittest.TestCase):
    
    def test_fun(self):
        self.assertEqual(fun(1,11), -55)

if __name__ == '__main__':
    unittest.main()
