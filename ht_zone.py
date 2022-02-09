from selenium import webdriver
from constants import *


def log_in(driver):
    username = driver.find_element_by_xpath(HT_USERNAME_BOX)
    username.send_keys(HT_USERNAME)
    password = driver.find_element_by_xpath(HT_PASSWORD_BOX)
    password.send_keys(HT_PASSWORD)
    id_num = driver.find_element_by_xpath(HT_ID_NUM_BOX)
    id_num.send_keys(HT_ID_NUM)
    button = driver.find_element_by_xpath(HT_BUTTON)
    button.click()


def get_ticket(driver, code):
    add_ticker = driver.find_element_by_xpath('//*[@id="addHtmlField"]/span/img')
    add_ticker.click()
    continue_button = driver.find_element_by_xpath('//*[@id="callpaymodal"]')
    continue_button.click()
    code_with_pin = driver.find_element_by_xpath('//*[@id="paymodal"]/div/div/div[2]/div/div[2]/div[1]/label[1]')
    code_with_pin.click()
    insert_code(driver, code)


def insert_code(driver, code):
    main_code, pin0 = seperate_code(code)
    code = driver.find_element_by_xpath('//*[@id="cardid"]')
    code.send_keys(main_code)
    pin = driver.find_element_by_xpath('//*[@id="pinnumber"]')
    pin.send_keys(pin0)
    submit_button = driver.find_element_by_xpath('//*[@id="paformsubmitmanual"]')
    submit_button.click()


def seperate_code(code):
    main_code = code[:8]
    pin = code[8:]
    return main_code, pin


def main(code):
    driver = webdriver.Chrome(PATH)
    driver.get(HT_LOGIN_LINK)
    driver.implicitly_wait(5)
    log_in(driver)
    get_ticket(driver, code)
    # return input("Enter code: ")





