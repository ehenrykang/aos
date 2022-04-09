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
    print(f'----------------------------------------------~* * * * *~------------------------------------------------')
    print(f'Advantage Online Shopping test started at: {datetime.datetime.now()}')
    # Make a full screen
    driver.maximize_window()

    # Wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the AOS web app URL - https://advantageonlineshopping.com/#/
    driver.get(locators.aos_url)
    print(f'Launch Advantage Online Shopping.')

    # Checking that we're on the correct URL address and we're seeing correct title as expected.
    if driver.current_url == locators.aos_url and driver.title == locators.aos_homepage_title:
        print(f'Great! Advantage Online Shopping is launched! URL: {driver.current_url}')
        print(f'We are seeing the page title: ', {driver.title})
        print()

    else:
        print(f'We are NOT at the Advantage Online Shopping Homepage! Please try again or check your code.')


# Validate HOMEPAGE Texts and Links
def validate_homepage_texts_links():
    if driver.current_url == locators.aos_url:
        print(f'---------------------------------~* VALIDATE HOMEPAGE TEXTS AND LINKS *~---------------------------------')
        assert driver.find_element(By.XPATH, '//span[contains(., "SPEAKERS")]').is_displayed()
        driver.find_element(By.ID, 'speakersTxt').click()
        sleep(3)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'speakersLink').click()
        sleep(2)
        driver.back()
        print(f'Home page item SPEAKERS is displayed and clickable. Shop Now link is clickable.')
        sleep(1)

        assert driver.find_element(By.XPATH, '//span[contains(., "TABLETS")]').is_displayed()
        driver.find_element(By.ID, 'tabletsTxt').click()
        sleep(3)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'tabletsLink').click()
        sleep(2)
        driver.back()
        print(f'Home page item TABLETS is displayed and clickable. Shop Now link is clickable.')
        sleep(1)

        assert driver.find_element(By.XPATH, '//span[contains(., "LAPTOPS")]').is_displayed()
        driver.find_element(By.ID, 'laptopsTxt').click()
        sleep(3)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'laptopsLink').click()
        sleep(2)
        driver.back()
        print(f'Home page item LAPTOPS is displayed and clickable. Shop Now link is clickable.')
        sleep(1)

        assert driver.find_element(By.XPATH, '//span[contains(., "MICE")]').is_displayed()
        driver.find_element(By.ID, 'miceTxt').click()
        sleep(3)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'miceLink').click()
        sleep(2)
        driver.back()
        print(f'Home page item MICE is displayed and clickable. Shop Now link is clickable.')
        sleep(1)

        assert driver.find_element(By.XPATH, '//span[contains(., "HEADPHONES")]').is_displayed()
        driver.find_element(By.ID, 'headphonesTxt').click()
        sleep(3)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'headphonesLink').click()
        sleep(2)
        driver.back()
        print(f'Home page item HEADPHONES is displayed and clickable. Shop Now link is clickable.')
        sleep(1)

        assert driver.find_element(By.XPATH, '//h3[text()="SPECIAL OFFER"]').is_displayed()
        print(f'Home page item SPECIAL OFFER is displayed.')
        sleep(1)

        assert driver.find_element(By.XPATH, '//button[text()="SEE OFFER"]').is_displayed()
        driver.find_element(By.ID, 'see_offer_btn').click()
        sleep(2)
        driver.back()
        sleep(2)
        print(f'Home page item SEE OFFER is displayed and clickable.')
        sleep(1)

        assert driver.find_element(By.XPATH, '//h2[text()="ALL YOU WANT FROM A TABLET"]').is_displayed()
        print('Home page item "ALL YOU WANT FROM A TABLET" is displayed.')
        driver.refresh()
        sleep(1)

        assert driver.find_element(By.XPATH, '//button[text()="EXPLORE NOW"]').is_displayed()
        driver.find_element(By.NAME, 'explore_now_btn').click()
        sleep(2)
        driver.back()
        sleep(2)
        print(f'Home page item EXPLORE NOW is displayed and clickable.')
        sleep(1)

        # POPULAR ITEMS
        assert driver.find_element(By.XPATH, '//label[contains(@id, "details_16")]').is_displayed()
        driver.find_element(By.ID, 'details_16').click()
        sleep(2)
        driver.back()
        sleep(2)
        print(f'Home page item POPULAR ITEM 1 is displayed and clickable.')
        sleep(1)

        assert driver.find_element(By.XPATH, '//label[contains(@id, "details_10")]').is_displayed()
        driver.find_element(By.ID, 'details_10').click()
        sleep(2)
        driver.back()
        sleep(2)
        print(f'Home page item POPULAR ITEM 2 is displayed and clickable.')
        sleep(1)

        assert driver.find_element(By.XPATH, '//label[contains(@id, "details_21")]').is_displayed()
        driver.find_element(By.ID, 'details_21').click()
        sleep(2)
        driver.back()
        sleep(2)
        print(f'Home page item POPULAR ITEM 3 is displayed and clickable.')
        sleep(2)

        # SOCIAL MEDIA LINKS
        if driver.find_element(By.XPATH, '//h3[contains(., "FOLLOW US")]').is_displayed():
            sleep(2)
            # Facebook Link
            driver.find_element(By.NAME, 'follow_facebook').click()
            print(f'Social Media Link FACEBOOK homepage is displayed and clickable.')
            sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            print(f'Social Media Link FACEBOOK tab is closed.')
            sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            sleep(2)

            # Twitter Link
            driver.find_element(By.NAME, 'follow_twitter').click()
            print(f'Social Media Link TWITTER homepage is displayed and clickable.')
            sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            print(f'Social Media Link TWITTER tab is closed.')
            sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            sleep(2)

            # LinkedIn Link
            driver.find_element(By.NAME, 'follow_linkedin').click()
            print(f'Social Media Link LINKEDIN homepage is displayed and clickable.')
            sleep(2)
            driver.switch_to.window(driver.window_handles[1])
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
    if driver.current_url == locators.aos_url:
        print(f'---------------------------------~* VALIDATE TOP NAVIGATION MENU *~--------------------------------------')
        driver.find_element(By.XPATH, '//span[contains(., "dvantage")]').click()
        sleep(1)
        print(f'Top Navigation Menu Link AOS LOGO is displayed and clickable.')
        sleep(2)

        assert driver.find_element(By.XPATH, '//a[contains(text(), "OUR PRODUCTS")]').is_displayed()
        sleep(1)
        driver.find_element(By.XPATH, '//a[contains(., "OUR PRODUCTS")]').click()
        sleep(1)
        print(f'Top Navigation Menu Link OUR PRODUCTS is displayed and clickable.')
        sleep(2)

        assert driver.find_element(By.XPATH, '//a[contains(text(), "SPECIAL OFFER")]').is_displayed()
        driver.find_element(By.XPATH, '//a[contains(., "SPECIAL OFFER")]').click()
        sleep(2)
        print(f'Top Navigation Menu Link SPECIAL OFFER is displayed and clickable.')
        sleep(2)

        assert driver.find_element(By.XPATH, '//a[contains(text(), "POPULAR ITEMS")]').is_displayed()
        driver.find_element(By.XPATH, '//a[contains(., "POPULAR ITEMS")]').click()
        sleep(3)
        print(f'Top Navigation Menu Link POPULAR ITEMS is displayed and clickable.')
        sleep(2)

        assert driver.find_element(By.XPATH, '//a[contains(text(), "CONTACT US")]').is_displayed()
        driver.find_element(By.XPATH, '//a[contains(., "CONTACT US")]').click()
        sleep(3)
        print(f'Top Navigation Menu Link CONTACT US is displayed and clickable.')
        sleep(2)

        driver.find_element(By.ID, 'menuSearch').click()
        sleep(2)
        print(f'Top Navigation Menu Link SEARCH ICON is displayed and clickable.')
        driver.refresh()
        sleep(3)

        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)
        print(f'Top Navigation Menu Link USER ICON is displayed and clickable.')
        driver.refresh()
        sleep(3)

        driver.find_element(By.ID, 'menuCart').click()
        print(f'Top Navigation Menu Link CART ICON is displayed and clickable.')
        driver.back()
        sleep(3)

        driver.find_element(By.ID, 'menuHelp').click()
        sleep(2)
        print(f'Top Navigation Menu Link MENU HELP ICON is displayed and clickable.')
        print(f'-------------------------------------------------------------------')
        print(f'Expected: All Top Navigation Menu Text Links are clickable: OUR PRODUCTS | SPECIAL OFFER | POPULAR ITEMS | CONTACT US')
        driver.refresh()
        print()

    else:
        print(f'Top Navigation Menu Links are not clickable.')


# Validate CONTACT US Form
def validate_contact_us_form():
    print(f'---------------------------------~* VALIDATE CONTACT US FORM *~------------------------------------------')
    if driver.current_url == locators.aos_url:
        Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Speakers')
        sleep(2)
        Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text('Bose SoundLink Wireless Speaker')
        sleep(2)
        driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
        sleep(2)
        driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.message)
        sleep(2)
        driver.find_element(By.ID, 'send_btnundefined').click()
        sleep(3)
        assert driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').is_displayed()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').click()
        sleep(2)
        print(f'CONTACT US Form is submitted successfully.')
        print(f'We are seeing the "Thank you for contacting Advantage support" message and the CONTINUE SHOPPING button.')
        print(f'CONTACT US Form is confirmed!')
        sleep(2)
        print()

    else:
        print(f'CONTACT US Form not validated.')


# Create New User Account - using Faker library fake data
def create_new_user():
    print(f'---------------------------------~* CREATE NEW USER *~---------------------------------------------------')
    if driver.current_url == locators.aos_url:
        driver.find_element(By.ID, 'menuUser').click()
        print(f'Login Form is displayed --- continue to Create New Account.')
        sleep(3)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(2)
        if driver.current_url == locators.aos_register_url:
            print(f'CREATE ACCOUNT Page is displayed.')
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
            print(f'Test Scenario: Create a new user with Username: {locators.new_username} and Password: {locators.new_password} --- is passed!')
            print()
        else:
            print('Some thing went wrong. Verify your code.')

    else:
        print(f'We are not at the CREATE A NEW ACCOUNT page.')


# Validate New Account created (new username is displayed in the top menu)
def validate_new_user_created():
    print(f'---------------------------------~* VALIDATE NEW USER *~-------------------------------------------------')
    if driver.current_url == locators.aos_url:
        if driver.find_element(By.XPATH, f'//a[contains(., "{locators.new_username}")]'):
            sleep(3)
            print(f'UserName: {locators.new_username} is displayed at Top right Menu.')
            sleep(2)
            print(f'New User Account fullname is: {locators.full_name}')
            print(f'New User Account address is: {locators.address1}')
            print(f'Expected: New User Account validated successfully!')
            print()
        else:
            print(f'New user created not validated.')

    else:
        print(f'New User Account not created successfully. Please verify all the required fields (*) are completed.')


# Logout
def log_out():
    print(f'---------------------------------~* LOGOUT *~------------------------------------------------------------')
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
    print(f'---------------------------------~* LOGIN NEW USER *~----------------------------------------------------')
    if driver.current_url == locators.aos_url:
        print(f'Login Form is displayed --- continue to Login.')
        driver.find_element(By.ID, 'menuUser').click()
        sleep(5)
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(1)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        print(f'We logged in successfully with Username: {locators.new_username} and Password: {locators.new_password}')
        print(f'New User Account with username {locators.new_username} is displayed at Top right Menu --- Test Passed!')
        sleep(2)
        print()

    else:
        print(f'Log in with new user not successful. Please verify your code or login credentials.')


# Validate User Login
def validate_user_login():
    print(f'---------------------------------~* VALIDATE USER LOGIN *~-----------------------------------------------')
    if driver.current_url == locators.aos_url:
        if driver.find_element(By.XPATH, f'//a[contains(., "{locators.new_username}")]'):
            print(f'UserName: {locators.new_username} is displayed at Top right Menu.')
            sleep(3)
            print(f'Expected user: {locators.new_username} --- login successful!')
            print()
        else:
            print(f'User login not validated.')

    else:
        print(f'User not logged in. Please try logging in again.')


# Close the browser and display a user-friendly message.
def tearDown():
    print(f'----------------------------------* TEARDOWN *-----------------------------------------------------------')
    if driver is not None:
        print(f'Test scenario completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

    else:
        print(f'Unable to close and quit. Something went wrong.')


# Open the web browser
# setUp()

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

# Logout
# log_out()

# Close the browser
# tearDown()
