# coding=utf-8

from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://10.6.2.80:5002")
loginusername = browser.find_element_by_xpath("//input[@type='text']")
loginuserpasswd = browser.find_element_by_xpath("//input[@type='password']")
loginsubmit = browser.find_element_by_id("btn")
loginusername.send_keys("root")
loginuserpasswd.send_keys("scutech")
loginsubmit.click()
