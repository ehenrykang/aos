import unittest
import aos_methods as methods


class AOSPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_aos():  # test_ in the name is mandatory
        methods.setup()
        methods.validate_homepage_texts_links()
        methods.validate_contact_us_form()
        methods.validate_top_nav_menu()
        methods.create_new_user()
        methods.validate_new_user_created()
        methods.log_out()
        methods.log_in()
        methods.validate_user_login()
        methods.checkout_shopping_cart()
        methods.log_out()
        methods.log_in()
        methods.validate_order()
        methods.delete_user_account()
        methods.log_in()
        methods.validate_user_account_deleted()
        methods.teardown()
