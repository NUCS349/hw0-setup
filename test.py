import unittest

class TestAssignment(unittest.TestCase):
    def test_environment(self):
        import numpy as np

    def test_sum_numbers(self):
        from code import sum_numbers
        self.assertEqual(sum_numbers(3, 5), 8)
        self.assertEqual(sum_numbers(5, 4), 9)
        self.assertEqual(sum_numbers(-1, 3), 2)

if __name__ == '__main__':
    suite = (unittest.TestLoader()
        .loadTestsFromTestCase(TestEnvironment))
    unittest.TextTestRunner(verbosity=2).run(suite)