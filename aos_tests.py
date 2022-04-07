import unittest
import aos_methods as methods


class AOSPositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_create_new_user(): # test_ in the name is mandatory
        methods.setUp()
        methods.create_new_user()
        methods.validate_new_user_created()
        methods.log_out()
        methods.log_in()
        methods.validate_user_login()
        methods.log_out()
        methods.tearDown()