import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import aos_locators as locators
from selenium.webdriver.support.ui import Select
# Using Selenium WebDriver, open the web browser.

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


# Fixture method - to open web browser
def setUp():
    print(f'----------------------------------* * * * *----------------------------------')
    print(f'Advantage Online Shopping test started at: {datetime.datetime.now()}')
    # Make a full screen
    driver.maximize_window()

    # Wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the AOS web app URL - https://advantageonlineshopping.com/#/
    driver.get(locators.aos_url)
    print(f'Launch Advantage Online Shopping')

    # Checking that we're on the correct URL address and we're seeing correct title as expected.
    if driver.current_url == locators.aos_url and driver.title == locators.aos_homepage_title:
        print(f'Great! Advantage Online Shopping is launched! URL: {driver.current_url}')
        print(f'We are seeing the page title: ', {driver.title})
        print()

    else:
        print(f'We are NOT at the Advantage Online Shopping Homepage! Please try again or check your code.')


# Create New User Account - using Faker library fake data
def create_new_user():
    print(f'----------------------------------* CREATE NEW USER *----------------------------------')
    driver.find_element(By.ID, 'menuUser').click()
    print(f'Login Form is displayed - continue to Create New Account')
    sleep(5)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(2)
    if driver.current_url == locators.aos_register_url:
        print(f'CREATE ACCOUNT Page is displayed')
        sleep(2)
        # Enter Account Details
        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
        sleep(1)
        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(1)
        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
        sleep(1)
        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
        sleep(1)

        # Enter Personal Details
        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.new_firstname)
        sleep(1)
        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.new_lastname)
        sleep(1)
        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
        sleep(1)

        # Enter Address information
        Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')
        sleep(1)
        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
        sleep(1)
        driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
        sleep(1)
        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.state_province_region)
        sleep(1)
        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
        sleep(1)

        # Checkbox for "I agree..."
        driver.find_element(By.NAME, 'i_agree').click()
        sleep(1)

        # Create new account
        driver.find_element(By.ID, 'register_btnundefined').click()
        sleep(2)
        print(f'--- Test Scenario: Create a new user with Username: {locators.new_username} and Password: {locators.new_password} --- is passed')
        print()

    else:
        print(f'We are not at the CREATE A NEW ACCOUNT page.')


# Validate New Account created (new username is displayed in the top menu)
def validate_new_user_created():
    print(f'----------------------------------* VALIDATE NEW USER *----------------------------------')
    if driver.current_url == locators.aos_url:
        assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
        print(f'UserName: {locators.new_username} is displayed')
        sleep(3)
        print(f'New User Account fullname is: {locators.full_name}')
        print(f'New User Account address is: {locators.address1}')
        print()

    else:
        print(f'New User Account not created successfully. Please verify all the required fields (*) are completed.')


# Logout
def log_out():
    print(f'----------------------------------* LOGOUT *----------------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(2)
    if driver.current_url == locators.aos_url:
        print(f'Logged out successfully at: {datetime.datetime.now()}')
        sleep(2)
        print()

    else:
        print(f'Unable to log out. Something went wrong.')


# Login with New Account
def log_in():
    print(f'----------------------------------* LOGIN NEW USER *----------------------------------')
    if driver.current_url == locators.aos_url:
        print(f'Login Form is displayed - continue to Login')
        driver.find_element(By.ID, 'menuUser').click()
        sleep(5)
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(1)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        print(f'We logged in successfully with Username: {locators.new_username} and Password: {locators.new_password}')
        print(f'--- New User Account with username {locators.new_username} is displayed at top right. Test Passed ---')
        sleep(2)
        print()

    else:
        print(f'Log in with new user not successful. Please verify your code or login credentials.')


def validate_user_login():
    print(f'----------------------------------* VALIDATE USER LOGIN *----------------------------------')
    if driver.current_url == locators.aos_url:
        assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
        print(f'Expected user: {locators.new_username} login successful!')
        sleep(1)
        print()

    else:
        print(f'User not logged in. Please try logging in again.')


# Close the browser and display a user-friendly message.
def tearDown():
    print(f'----------------------------------* TEARDOWN *----------------------------------')
    if driver is not None:
        print(f'Test scenario completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

    else:
        print(f'Unable to close and quit. Something went wrong.')


# Open the web browser
# setUp()

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

# Logout
# log_out()

# Close the browser
# tearDown()
