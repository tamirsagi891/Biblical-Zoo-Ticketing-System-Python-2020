from selenium import webdriver
from constants import *
import time


def log_in(driver):
    username = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/form/div/div[1]/div/input')
    username.send_keys('תנכי')
    password = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/form/div/div[2]/div/input')
    password.send_keys('9937')
    button = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[3]/div[1]/button')
    button.click()


def get_ticket(driver, code):
    search_box = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/form/div[2]/input')
    search_box.send_keys(code)
    search_button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/form/div[3]/button')
    search_button.click()


def main(code):
    driver = webdriver.Chrome(PATH)
    driver.get(CN_LOGIN_LINK)
    driver.implicitly_wait(5)
    log_in(driver)
    get_ticket(driver, code)
    # return input("Enter code: ")
