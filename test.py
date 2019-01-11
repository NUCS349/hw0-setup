import unittest

class TestEnvironment(unittest.TestCase):
    def test_environment(self):
        import numpy as np

if __name__ == '__main__':
    suite = (unittest.TestLoader()
        .loadTestsFromTestCase(TestEnvironment))
    unittest.TextTestRunner(verbosity=2).run(suite)