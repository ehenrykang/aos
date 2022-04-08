from faker import Faker
fake = Faker(locale='en_CA')
aos_url = 'https://advantageonlineshopping.com/#/'
aos_title = 'Advantage Shopping'
aos_homepage_title = '\xa0Advantage Shopping'
aos_register_url = 'https://advantageonlineshopping.com/#/register'
aos_login_url = 'https://advantageonlineshopping.com/#/'
new_username = f'{fake.user_name()[:12]}{fake.pyint(111,999)}'
new_password = fake.password()[:12]
new_firstname = fake.first_name()
new_lastname = fake.last_name()
email = fake.email()
phone = fake.phone_number()
city = fake.city()
full_name = f'{new_firstname} {new_lastname}'
address1 = f'{fake.street_address()}, {city}, {fake.province_abbr()}, {fake.current_country()} {fake.postalcode_in_province()}'
address = fake.street_address()
postal_code = fake.postalcode_in_province()
state_province_region = fake.province_abbr()
country = fake.current_country()
aos_username = f'{fake.user_name()}{fake.pyint(111,999)}'
aos_password = f'{fake.password()[:12]}'
new_user_url = 'https://advantageonlineshopping.com/#/myAccount'
message = fake.sentence(nb_words=20)