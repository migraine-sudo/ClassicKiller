from selenium import webdriver
from Click.Click import *

def Login(username,password):

        browser=webdriver.Firefox()
        browser.get("http://ibook.cslg.cn/Exam")
        #print browser.page_source

        text_username=browser.find_element_by_class_name("username")
        text_password=browser.find_element_by_class_name("password")
        #btn_submit=browser.find_element_by_class_name("submit")


        text_username.send_keys(username)
        text_password.send_keys(password)
        Click_Submit(browser)
        #btn_submit.click()

        browser.get("http://ibook.cslg.cn/Home/Exam")

        return browser
