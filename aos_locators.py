from faker import Faker
import random
fake = Faker(locale='en_CA')
aos_url = 'https://advantageonlineshopping.com/#/'
aos_orders_url = 'https://advantageonlineshopping.com/#/MyOrders'
aos_orderpayment_url = 'https://advantageonlineshopping.com/#/orderPayment'
aos_title = 'Advantage Shopping'
aos_homepage_title = '\xa0Advantage Shopping'
aos_register_url = 'https://advantageonlineshopping.com/#/register'
aos_login_url = 'https://advantageonlineshopping.com/#/'
aos_cart_url = 'https://advantageonlineshopping.com/#/shoppingCart'
new_username = f'{fake.user_name()[:10]}{fake.pyint(111,999)}'
new_password = fake.password()[:10]
new_firstname = fake.first_name()
new_lastname = fake.last_name()
email = fake.email()
phone = fake.phone_number()
city = fake.city()
full_name = f'{new_firstname} {new_lastname}'
postal_code = fake.postalcode_in_province()
address1 = f'{fake.street_address()}, {city}, {fake.province_abbr()}, {fake.current_country()} {postal_code}'
address = fake.street_address()
state_province_region = fake.province_abbr()
country = fake.current_country()
aos_username = f'{fake.user_name()[:8]}{fake.pyint(11,99)}'
aos_password = f'{fake.password()[:10]}'
new_user_url = 'https://advantageonlineshopping.com/#/myAccount'
message = fake.sentence(nb_words=20)
order_id = ""
item_number = random.choice([i for i in range(1, 35) if i != 13])
aos_product_url = f'{aos_url}product/{item_number}'
facebook_url = 'https://www.facebook.com/MicroFocus/'
twitter_url = 'https://twitter.com/MicroFocus'
linkedin_url = 'https://www.linkedin.com/company/micro-focus/'
