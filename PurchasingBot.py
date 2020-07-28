from config import keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
# note: takes approximately 1.7 seconds to pull up the webpage.

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time()*1000))
        result = method(*args, **kw)
        endTime = int(round(time.time()*1000))
        print("Execution tme: {}".format((endTime - startTime)/1000))
        return result
    return wrapper

@timeme
def order(drive, k):
    drive.get(k['product_url'])

    # use inspect element, do 'copy by xpath' on the specific element
    drive.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(.1)
    drive.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

    drive.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k['name'])
    drive.find_element_by_xpath('//*[@id="order_email"]').send_keys(k['email'])
    drive.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k['phone_number'])
    drive.find_element_by_xpath('//*[@id="bo"]').send_keys(k['address'])
    drive.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k['zip'])
    drive.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(k['card_num'])
    drive.find_element_by_xpath('//*[@id="credit_card_month"]/option[3]').click()
    drive.find_element_by_xpath('//*[@id="credit_card_year"]/option[5]').click()
    drive.find_element_by_xpath('//*[@id="orcer"]').send_keys(k['cvv'])

    # # necessary for terms and conditions, process payment
    drive.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
    drive.find_element_by_xpath('//*[@id="pay"]/input').click()

if __name__ == '__main__':
    driver = webdriver.Chrome(keys["chromdriver_path"])
    order(driver, keys)
