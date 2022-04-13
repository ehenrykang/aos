import datetime
from time import sleep
from selenium import webdriver
import aos_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException

# Using Selenium WebDriver, open the web browser.
s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


# Fixture method - to open web browser
def setup():
    print(f'*----------------------------------------------~*~*~*~*~*~----------------------------------------------*')
    print(f'Advantage Online Shopping test started at: {datetime.datetime.now()}')
    # Make a full screen
    driver.maximize_window()

    # Wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the AOS web app URL - https://advantageonlineshopping.com/#/
    driver.get(locators.aos_url)
    print(f'Launch Advantage Online Shopping.')

    # Checking that we're on the correct URL address, and we're seeing the correct title as expected.
    if driver.current_url == locators.aos_url and driver.title == locators.aos_homepage_title:
        print(f'Great! Advantage Online Shopping is launched! URL: {driver.current_url}')
        print(f'We are seeing the page title:', {driver.title})
        print()

    else:
        print(f'We are NOT at the Advantage Online Shopping Homepage! Please try again or check your code.')


# Validate HOMEPAGE Texts and Links
def validate_homepage_texts_links():
    print(f'*--------------------------------~* VALIDATE HOMEPAGE TEXTS AND LINKS *~--------------------------------*')
    if driver.current_url == locators.aos_url:
        sleep(1)
        # Validate SPEAKERS text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//span[contains(., "SPEAKERS")]').is_displayed()
        driver.find_element(By.ID, 'speakersTxt').click()
        sleep(2.5)
        driver.back()
        sleep(1.5)
        # Validate the SPEAKERS 'Shop Now' link is clickable
        driver.find_element(By.ID, 'speakersLink').click()
        sleep(1.5)
        driver.back()
        print(f'Home page item SPEAKERS is displayed and clickable. Shop Now link is clickable.')
        sleep(1)

        # Validate TABLETS text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//span[contains(., "TABLETS")]').is_displayed()
        driver.find_element(By.ID, 'tabletsTxt').click()
        sleep(2.5)
        driver.back()
        sleep(1.5)
        # Validate the TABLETS 'Shop Now' link is clickable
        driver.find_element(By.ID, 'tabletsLink').click()
        sleep(1.5)
        driver.back()
        print(f'Home page item TABLETS is displayed and clickable. Shop Now link is clickable.')
        sleep(1)

        # Validate LAPTOPS text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//span[contains(., "LAPTOPS")]').is_displayed()
        driver.find_element(By.ID, 'laptopsTxt').click()
        sleep(2.5)
        driver.back()
        sleep(1.5)
        # Validate the LAPTOPS 'Shop Now' link is clickable
        driver.find_element(By.ID, 'laptopsLink').click()
        sleep(1.5)
        driver.back()
        print(f'Home page item LAPTOPS is displayed and clickable. Shop Now link is clickable.')
        sleep(1)

        # Validate MICE text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//span[contains(., "MICE")]').is_displayed()
        driver.find_element(By.ID, 'miceTxt').click()
        sleep(2.5)
        driver.back()
        sleep(1.5)
        # Validate the MICE 'Shop Now' link is clickable
        driver.find_element(By.ID, 'miceLink').click()
        sleep(1.5)
        driver.back()
        print(f'Home page item MICE is displayed and clickable. Shop Now link is clickable.')
        sleep(1)

        # Validate HEADPHONES text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//span[contains(., "HEADPHONES")]').is_displayed()
        driver.find_element(By.ID, 'headphonesTxt').click()
        sleep(2.5)
        driver.back()
        sleep(1.5)
        # Validate the HEADPHONES 'Shop Now' link is clickable
        driver.find_element(By.ID, 'headphonesLink').click()
        sleep(1.5)
        driver.back()
        print(f'Home page item HEADPHONES is displayed and clickable. Shop Now link is clickable.')
        sleep(1)

        # Validate SPECIAL OFFER text is displayed
        assert driver.find_element(By.XPATH, '//h3[text()="SPECIAL OFFER"]').is_displayed()
        print(f'Home page item SPECIAL OFFER is displayed.')
        sleep(3.5)

        # Validate SEE OFFER text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//button[text()="SEE OFFER"]').is_displayed()
        driver.find_element(By.ID, 'see_offer_btn').click()
        sleep(1.5)
        print(f'Home page item SEE OFFER is displayed and clickable.')
        driver.back()
        driver.refresh()
        sleep(2.5)

        # Validate ALL YOU WANT FROM A TABLET text is displayed
        assert driver.find_element(By.XPATH, '//h2[text()="ALL YOU WANT FROM A TABLET"]').is_displayed()
        print('Home page item "ALL YOU WANT FROM A TABLET" is displayed.')
        driver.refresh()
        sleep(2)

        # Validate EXPLORE NOW text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//button[text()="EXPLORE NOW"]').is_displayed()
        driver.find_element(By.NAME, 'explore_now_btn').click()
        sleep(1.5)
        driver.back()
        sleep(1.5)
        print(f'Home page item EXPLORE NOW is displayed and clickable.')
        sleep(1)

        # POPULAR ITEMS
        # Popular Item 1
        assert driver.find_element(By.XPATH, '//label[contains(@id, "details_16")]').is_displayed()
        driver.find_element(By.ID, 'details_16').click()
        sleep(1.5)
        driver.back()
        sleep(1.5)
        print(f'Home page item POPULAR ITEM 1 is displayed and clickable.')
        sleep(1)

        # Popular Item 2
        assert driver.find_element(By.XPATH, '//label[contains(@id, "details_10")]').is_displayed()
        driver.find_element(By.ID, 'details_10').click()
        sleep(1.5)
        driver.back()
        sleep(1.5)
        print(f'Home page item POPULAR ITEM 2 is displayed and clickable.')
        sleep(1)

        # Popular Item 3
        assert driver.find_element(By.XPATH, '//label[contains(@id, "details_21")]').is_displayed()
        driver.find_element(By.ID, 'details_21').click()
        sleep(1.5)
        driver.back()
        sleep(1.5)
        print(f'Home page item POPULAR ITEM 3 is displayed and clickable.')
        sleep(2)

        # VALIDATE SOCIAL MEDIA LINKS
        if driver.find_element(By.XPATH, '//h3[contains(., "FOLLOW US")]').is_displayed():
            sleep(2)
            # Facebook Link
            driver.find_element(By.NAME, 'follow_facebook').click()
            driver.switch_to.window(driver.window_handles[1])
            if driver.current_url == locators.facebook_url:
                print(f'Social Media Link FACEBOOK homepage is displayed and clickable.')
                sleep(2)
            else:
                print(f'Twitter link is not reachable')
            driver.close()
            print(f'Social Media Link FACEBOOK tab is closed.')
            sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            sleep(2)

            # Twitter Link
            driver.find_element(By.NAME, 'follow_twitter').click()
            driver.switch_to.window(driver.window_handles[1])
            if driver.current_url == locators.twitter_url:
                print(f'Social Media Link TWITTER homepage is displayed and clickable.')
                sleep(2)
            else:
                print(f'Twitter link is not reachable')
            driver.close()
            print(f'Social Media Link TWITTER tab is closed.')
            sleep(1.5)
            driver.switch_to.window(driver.window_handles[0])
            sleep(2)

            # LinkedIn Link
            driver.find_element(By.NAME, 'follow_linkedin').click()
            driver.switch_to.window(driver.window_handles[1])
            if driver.current_url == locators.linkedin_url:
                print(f'Social Media Link LINKEDIN homepage is displayed and clickable.')
                sleep(2)
            else:
                print(f'LinkedIn link is not reachable. Please check your code.')
            driver.close()
            print(f'Social Media Link LINKEDIN tab is closed.')
            sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            sleep(1)
            print()

        else:
            print(f'Social Media Links not reachable. Please check the link again.')

    else:
        print(f'Homepage Links are not clickable.')


# Validate TOP NAVIGATION Menu
def validate_top_nav_menu():
    print(f'*----------------------------------~* VALIDATE TOP NAVIGATION MENU *~-----------------------------------*')
    if driver.current_url == locators.aos_url:
        # Validate ADVANTAGE LOGO link
        sleep(1)
        driver.find_element(By.XPATH, '//span[contains(., "dvantage")]').click()
        sleep(1)
        print(f'Top Navigation Menu Link ADVANTAGE LOGO is displayed and clickable.')
        sleep(2)

        # Validate OUR PRODUCTS link
        assert driver.find_element(By.XPATH, '//a[contains(text(), "OUR PRODUCTS")]').is_displayed()
        sleep(1)
        driver.find_element(By.XPATH, '//a[contains(., "OUR PRODUCTS")]').click()
        sleep(1)
        print(f'Top Navigation Menu Link OUR PRODUCTS is displayed and clickable.')
        sleep(1.5)

        # Validate SPECIAL OFFER link
        assert driver.find_element(By.XPATH, '//a[contains(text(), "SPECIAL OFFER")]').is_displayed()
        driver.find_element(By.XPATH, '//a[contains(., "SPECIAL OFFER")]').click()
        sleep(1.5)
        print(f'Top Navigation Menu Link SPECIAL OFFER is displayed and clickable.')
        sleep(1.5)

        # Validate POPULAR ITEMS link
        assert driver.find_element(By.XPATH, '//a[contains(text(), "POPULAR ITEMS")]').is_displayed()
        driver.find_element(By.XPATH, '//a[contains(., "POPULAR ITEMS")]').click()
        sleep(2.5)
        print(f'Top Navigation Menu Link POPULAR ITEMS is displayed and clickable.')
        sleep(1.5)

        # Validate CONTACT US link
        assert driver.find_element(By.XPATH, '//a[contains(text(), "CONTACT US")]').is_displayed()
        driver.find_element(By.XPATH, '//a[contains(., "CONTACT US")]').click()
        sleep(2.5)
        print(f'Top Navigation Menu Link CONTACT US is displayed and clickable.')
        sleep(1.5)

        # Validate SEARCH ICON link
        driver.find_element(By.ID, 'menuSearch').click()
        sleep(1.5)
        print(f'Top Navigation Menu Link SEARCH ICON is displayed and clickable.')
        driver.refresh()
        sleep(2.5)

        # Validate USER ICON link
        driver.find_element(By.ID, 'menuUser').click()
        sleep(1.5)
        print(f'Top Navigation Menu Link USER ICON is displayed and clickable.')
        driver.refresh()
        sleep(2.5)

        # Validate CART ICON link
        driver.find_element(By.ID, 'menuCart').click()
        print(f'Top Navigation Menu Link CART ICON is displayed and clickable.')
        driver.back()
        sleep(1)
        driver.find_element(By.XPATH, '//h3[contains(text(), "SHOPPING CART")]').click()
        sleep(5)

        # Validate HELP ICON link
        driver.find_element(By.ID, 'menuHelp').click()
        sleep(1)
        print(f'Top Navigation Menu Link MENU HELP ICON is displayed and clickable.')
        print(f'-------------------------------------------------------------------')
        print(f'Expected: All Top Navigation Menu Text Links are clickable:')
        print(f'          OUR PRODUCTS | SPECIAL OFFER | POPULAR ITEMS | CONTACT US')
        driver.refresh()
        print()

    else:
        print(f'Top Navigation Menu Links are not clickable.')


# Validate CONTACT US Form
def validate_contact_us_form():
    print(f'*------------------------------------~* VALIDATE CONTACT US FORM *~-------------------------------------*')
    if driver.current_url == locators.aos_url:
        sleep(1)
        Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Speakers')
        sleep(1.5)
        Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text('Bose SoundLink Wireless Speaker')
        sleep(1.5)
        driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
        sleep(1.5)
        driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.message)
        sleep(1.5)

        # Submit CONTACT US Form
        driver.find_element(By.ID, 'send_btnundefined').click()
        sleep(2.5)

        # Validate CONTACT US Form submission
        assert driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').is_displayed()
        sleep(1.5)
        driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').click()
        sleep(1.5)
        print(f'CONTACT US Form is submitted successfully.')
        print(f'We are seeing the "Thank you for contacting Advantage support" message and the CONTINUE SHOPPING button.')
        print(f'Test scenario --- CONTACT US Form validation --- is passed!')
        sleep(1.5)
        print()

    else:
        print(f'CONTACT US Form not validated.')


# Create New User Account - using Faker library fake data
def create_new_user():
    print(f'*-----------------------------------------~* CREATE NEW USER *~-----------------------------------------*')
    if driver.current_url == locators.aos_url:
        sleep(1)
        driver.find_element(By.ID, 'menuUser').click()
        print(f'Login Form is displayed --- continue to Create New Account.')
        sleep(2)

        # Click on CREATE NEW ACCOUNT link
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(1)
        if driver.current_url == locators.aos_register_url:
            print(f'CREATE ACCOUNT Page is displayed.')
            sleep(1)
            # Enter Account Details
            driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
            sleep(0.5)
            driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
            sleep(0.5)
            driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
            sleep(0.5)
            driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
            sleep(1)

            # Enter Personal Details
            driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.new_firstname)
            sleep(0.5)
            driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.new_lastname)
            sleep(0.5)
            driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
            sleep(1)

            # Enter Address information
            Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')
            sleep(1)
            driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
            sleep(0.5)
            driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
            sleep(0.5)
            driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.state_province_region)
            sleep(0.5)
            driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
            sleep(1)

            # Checkbox for "I agree..."
            driver.find_element(By.NAME, 'i_agree').click()
            sleep(0.5)

            # Create new account
            driver.find_element(By.ID, 'register_btnundefined').click()
            sleep(1.5)
            print(f'Test Scenario: Create a new user with Username: {locators.new_username} and Password: {locators.new_password} --- is passed!')
            print()
        else:
            print('Some thing went wrong. Verify your code.')

    else:
        print(f'We are not at the CREATE A NEW ACCOUNT page.')


# Validate New Account created (new username is displayed in the top menu)
def validate_new_user_created():
    print(f'*------------------------------------~* VALIDATE NEW USER CREATED *~------------------------------------*')
    if driver.current_url == locators.aos_url:
        sleep(1)
        if driver.find_element(By.XPATH, f'//a[contains(., "{locators.new_username}")]'):
            sleep(3)
            print(f'Username: {locators.new_username} is displayed at Top right Menu.')
            sleep(2)
            print(f'New User account fullname is: {locators.full_name}')
            print(f'New User account address is: {locators.address1}')
            print(f'Expected: New User account with username {locators.new_username} validated successfully!')
            print()
        else:
            print(f'New user created not validated.')

    else:
        print(f'New User Account not created successfully. Please verify all the required fields (*) are completed.')


# Checkout Shopping Cart
def checkout_shopping_cart():
    print(f'*-------------------------------------~* CHECKOUT SHOPPING CART *~--------------------------------------*')
    if driver.current_url == locators.aos_login_url and driver.title == locators.aos_homepage_title:
        # Randomly select an item to add to cart
        sleep(1)
        driver.get(locators.aos_product_url)
        sleep(1)
        driver.find_element(By.NAME, 'save_to_cart').click()
        sleep(1)
        driver.find_element(By.ID, 'shoppingCartLink').click()
        if driver.find_element(By.XPATH, '//label[@class="roboto-regular ng-binding"]'):
            print('Item added to cart successfully!')
        else:
            print('Item not added to cart. Something went wrong.')

        # Checkout the shopping cart
        driver.find_element(By.ID, 'checkOutButton').click()
        sleep(1)
        assert driver.find_element(By.XPATH, '//h3[contains(text(), "ORDER PAYMENT")]').is_displayed()
        print(f'Fullname of user: {locators.full_name}')
        driver.find_element(By.ID, 'next_btn').click()
        sleep(1)

        # Payment Method
        driver.find_element(By.NAME, 'safepay').send_keys(Keys.ENTER)
        sleep(0.5)
        driver.find_element(By.NAME, 'safepay_username').send_keys(locators.aos_username)
        sleep(1)
        driver.find_element(By.NAME, 'safepay_password').send_keys(locators.aos_password)
        sleep(1)
        driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
        sleep(1)
        assert driver.find_element(By.XPATH, '//h3[contains(text(), "ORDER PAYMENT")]').is_displayed()
        sleep(1)

        # Checkout completed
        assert driver.find_element(By.XPATH, '//span[contains(text(), "Thank you for buying with Advantage")]').is_displayed()
        sleep(1)
        locators.order_id = driver.find_element(By.ID, 'orderNumberLabel').text
        print(f"Tracking number: {driver.find_element(By.ID, 'trackingNumberLabel').text} and Order number: {locators.order_id}")
        if driver.current_url == locators.aos_orderpayment_url:
            sleep(1)
            print(f'Full details of user:')
            print(f' - Fullname: {locators.full_name}')
            print(f' - Phone number: {locators.phone}')
            print(f' - Address: {locators.address1}')
            print(f' - Date ordered: {datetime.datetime.now()}')
            print(f'Expected: Test scenario --- Checkout Shopping Cart --- completed successfully!')
            print()
        else:
            print(f'Fullname and address not validated.')

    else:
        print(f'Shopping Cart not checked out.')


# Validate Order
def validate_order():
    print(f'*-----------------------------------------~* VALIDATE ORDER *~------------------------------------------*')
    if driver.current_url == locators.aos_orders_url or driver.title == locators.aos_homepage_title:
        sleep(1)
        if driver.find_element(By.XPATH, f'//a[contains(., "{locators.new_username}")]'):
            print(f'Username: {locators.new_username} is displayed at Top right Menu.')
            sleep(1)
            print(f'Expected user with username: {locators.new_username} --- login successful!')
        else:
            print(f'User login not validated.')

        # Access user 'My Order' account
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()
        sleep(1)

        # Confirm order is displayed
        order_element = driver.find_element(By.XPATH, f'//label[contains(text(), "{locators.order_id}")]')
        assert order_element.is_displayed()
        sleep(1)
        print(f'Test scenario --- validate order is displayed --- confirmed!')
        print(f'*-------------------~* DELETE ORDER *~---------------------*')
        sleep(1)

        # Delete order from user account
        driver.find_element(By.XPATH, '//a[contains(text(), "REMOVE")]').click()
        sleep(1)
        # Confirm deletion of order
        driver.find_element(By.ID, 'confBtn_1').click()
        sleep(1)

        # Validate order deleted successfully
        try:
            assert order_element.is_displayed()
        except (AssertionError, StaleElementReferenceException):
            print(f'Element is not found:')
            print(f'- Order with order number {locators.order_id} does not exist.')
            print(f'- Test scenario --- order deleted successfully --- confirmed!')
            print()

    else:
        print('Order not validated. Please check your order number again.')


# Logout
def log_out():
    print(f'*---------------------------------------------~* LOGOUT *~----------------------------------------------*')
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(1)
    if driver.current_url == locators.aos_url:
        print(f'Logged out successfully at: {datetime.datetime.now()}')
        sleep(1)
        print()

    else:
        print(f'Unable to log out. Something went wrong.')


# Login with New Account
def log_in():
    print(f'*-----------------------------------------~* LOGIN NEW USER *~------------------------------------------*')
    if driver.current_url == locators.aos_url:
        sleep(2)
        print(f'Login Form is displayed --- continue to Login.')
        driver.find_element(By.ID, 'menuUser').click()
        sleep(4)
        # Enter user account credentials
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(1)
        # Authenticate user login
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(2.5)
        print()

    else:
        print(f'Log in with new user not successful. Please verify your code or login credentials.')


# Validate User Login
def validate_user_login():
    print(f'*---------------------------------------~* VALIDATE USER LOGIN *~---------------------------------------*')
    if driver.current_url == locators.aos_url:
        sleep(1)
        if driver.find_element(By.XPATH, f'//a[contains(., "{locators.new_username}")]'):
            print(f'Username: {locators.new_username} is displayed at Top right Menu.')
            sleep(1.5)
            print(f'Expected user: {locators.new_username} --- login successful!')
            print()
        else:
            print(f'User login not validated.')

    else:
        print(f'User not logged in. Please try logging in again.')


# Delete User Account
def delete_user_account():
    print(f'*---------------------------------------~* DELETE USER ACCOUNT *~---------------------------------------*')
    if driver.current_url == locators.aos_orders_url:
        sleep(1)
        if driver.find_element(By.XPATH, f'//a[contains(., "{locators.new_username}")]'):
            print(f'Username: {locators.new_username} is displayed at Top right Menu.')
            sleep(2)
        else:
            print(f'User login not validated.')

        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        # Access user account details
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
        sleep(1)

        # Account details page before deletion
        assert driver.find_element(By.XPATH, f'//label[contains(., "{locators.full_name}")]').is_displayed()
        sleep(3)
        print(f'Account details page for user: "{locators.full_name}" is displayed.')
        assert driver.find_element(By.XPATH, '//button[contains(., "Delete Account")]').is_displayed()
        popup = driver.find_element(By.XPATH, '//button[contains(., "Delete Account")]').is_displayed()
        print(f'Delete popup is displayed: {popup}')
        sleep(2)

        # Click the Delete Account button
        driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
        sleep(5)

        # Delete Confirmation screen
        assert driver.find_element(By.XPATH, '//*[contains(@class, "deletePopupBtn deleteRed")]').is_displayed()
        popup1 = driver.find_element(By.XPATH, '//*[contains(@class, "deletePopupBtn deleteRed")]').is_displayed()
        print(f'Delete Confirmation screen is displayed: {popup1}')
        sleep(2)

        # Confirm deletion of account
        driver.find_element(By.XPATH, '//*[contains(@class, "deletePopupBtn deleteRed")]').click()
        sleep(3)
        print(f'Confirmation message is displayed: Account deleted successfully.')
        print(f'User {locators.full_name} with email address {locators.email} is deleted!')
        print()

    else:
        print(f'User not logged in. Please try logging in again.')


# Validate User Account Deleted
def validate_user_account_deleted():
    print(f'*----------------------------------~* VALIDATE USER ACCOUNT DELETED *~----------------------------------*')
    if driver.current_url == locators.aos_url:
        print(f'Login Form is displayed --- continue to Login.')
        sleep(4)
        error_text = driver.find_element(By.ID, 'signInResultMessage').text
        assert error_text == 'Incorrect user name or password.'
        print(f'Username: {locators.new_username} and Password: {locators.new_password} is not found. Error: {error_text}')
        print(f'Test scenario --- Username {locators.new_username} deleted successfully --- Test Passed!')
        sleep(2)
        print()

    else:
        print(f'Account not deleted.')


# Close the browser and display a user-friendly message.
def teardown():
    print(f'*----------------------------------------------~*~*~*~*~*~----------------------------------------------*')
    if driver is not None:
        print(f'Test scenario completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

    else:
        print(f'Unable to close and quit. Something went wrong.')


# Open the web browser
# setup()

# Validate_homepage_texts_links
# validate_homepage_texts_links()

# Validate_top_nav_menu
# validate_top_nav_menu()

# Validate_contact_us_form
# validate_contact_us_form()

# Create New User
# create_new_user()

# Validate New User created
# validate_new_user_created()

# Logout
# log_out()

# Login
# log_in()

# Validate User Login
# validate_user_login()

# Checkout Shopping Cart
# checkout_shopping_cart()

# Validate Order
# validate_order()

# Delete User Account
# delete_user_account()

# Validate User Account Deleted
# validate_user_account_deleted()

# Logout
# log_out()

# Close the browser
# teardown()
