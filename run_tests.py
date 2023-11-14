# run_tests.py
import unittest

# Discover and run the tests
if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')

    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
