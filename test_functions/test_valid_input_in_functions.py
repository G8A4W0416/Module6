import unittest
from more_functions import validate_input_in_functions


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual("Greg: 0", validate_input_in_functions.score_input("Greg"))

    def test_score_input_test_score_valid(self):
        self.assertEqual("Greg: 100", validate_input_in_functions.score_input("Greg", 100))

    def test_score_input_test_score_below_range(self):
        self.assertEqual("Invalid test score, try again!", validate_input_in_functions.score_input("Greg", -1))

    def test_score_input_test_score_above_range(self):
        self.assertEqual("Invalid test score, try again!", validate_input_in_functions.score_input("Greg", 101))

    def test_score_input_test_score_non_numeric(self):
        self.assertEqual("Invalid test score, try again!", validate_input_in_functions.score_input("Greg", "Wilhelm"))

    def test_score_input_invalid_message(self):
        self.assertEqual("Please enter a value between 0-100",
                         validate_input_in_functions.score_input("Greg", 100, "Please enter a value between 0-100"))


if __name__ == '__main__':
    unittest.main()
