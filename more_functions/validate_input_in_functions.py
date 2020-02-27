def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """ This takes in a test name, test score, and invalid message. The user is prompted for a valid test score until it
    is in the range of 0-100, then prints out the valid input as 'Test name: ##'.
    :param test_name: String name passed in
    :param test_score: Int score passed in. Optional, with default value of 0 (zero)
    :param invalid_message: String invalid message passed in. Optional, with default value of
    'Invalid test score, try again!'
    :return: String showing test name with valid test score
    """

    while True:
        if 0 <= test_score <= 100:
            break
        else:
            return invalid_message

    return test_name + ": " + str(test_score)
