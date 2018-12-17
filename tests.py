import unittest 
from search import search
from mobile_operator import Operator
  
class SimpleTest(unittest.TestCase): 
   
    def test_operator(self):
        """Method to test Operator class and its method"""

        prices_a = {'123': 0.9, '1234': 0.3, '765': 0.2, '7237283': 0.8}
        a = Operator('A', prices_a)
        self.assertEqual(a.get_price('123'), 0.9)

    def test_search(self):
        """Method to test search function"""

        prices_a = {'123': 0.9, '1234': 0.3, '765': 0.2, '7237283': 0.8}
        prices_b = {'1234': 0.1, '3456': 0.3, '9876': 0.2, '75243928': 0.8}
        a = Operator('A', prices_a)
        b = Operator('B', prices_b)
        operators = []
        operators.append(a)
        operators.append(b)
        cheapest_price, cheapest_operator = search(operators, '+123456782345')
        
        self.assertEqual(cheapest_price, 0.1)
        self.assertEqual(cheapest_operator, 'B') 
  
if __name__ == '__main__': 
    unittest.main() 
