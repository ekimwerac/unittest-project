Let's break down the main features of Python 3 unittest using an example of a Calculator class. We'll structure the example with multiple files to showcase how tests can be organized. The directory tree will have a clear separation between the source code and the test code.

Directory Tree:

project/
|-- calculator/
|   |-- __init__.py
|   |-- calculator.py
|-- tests/
|   |-- __init__.py
|   |-- test_calculator.py
|-- run_tests.py

Explanation:
Calculator Class (calculator/calculator.py):

This file contains the implementation of the Calculator class with basic arithmetic operations.
Test Cases (tests/test_calculator.py):

This file contains test cases for the Calculator class using the unittest framework.
Test methods start with "test_" and use various assertion methods (self.assertEqual, self.assertRaises) to check the correctness of the calculator methods.
setUp and tearDown methods, if defined, run before and after each test, providing a way to set up and clean up resources.
Test Runner (run_tests.py):

This file serves as the entry point for running tests.
It imports the unittest module and uses the TestLoader to discover test files matching the pattern test_*.py in the tests directory.
The TextTestRunner is used to run the tests, and the results are printed to the console.

Execution:
To run the tests, you can execute the run_tests.py script. This script will discover and run all test files in the tests directory, including test_calculator.py. The directory structure allows for a clear separation between the source code and the test code, making it easy to manage and organize the project.
