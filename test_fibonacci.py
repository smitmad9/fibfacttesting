import unittest
import fibonacci

class testFib (unittest.TestCase):
    
    def testFib(self): 
        self.assertEqual(fibonacci.nthfib(0), 0)
        self.assertEqual(fibonacci.nthfib(1), 1)
        self.assertEqual(fibonacci.nthfib(2), 1)
        self.assertEqual(fibonacci.nthfib(3), 2)
        self.assertEqual(fibonacci.nthfib(-1), None)

    def testFact(self):
        self.assertEqual(fibonacci.nthfib(0), 0)
        self.assertEqual(fibonacci.nthfib(1), 1)
        self.assertEqual(fibonacci.nthfib(2), 1)
        self.assertEqual(fibonacci.nthfib(3), 2)
        self.assertEqual(fibonacci.nthfib(-1), None)


if __name__ == '__main__':
    unittest.main(verbosity=2)