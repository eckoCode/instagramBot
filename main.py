import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains


print('Setting the capabilities')
capabilities = DesiredCapabilities.FIREFOX
capabilities["marionette"] = True
firefox_bin = "/usr/bin/firefox"

options = Options()
options.headless = True  # If you want to enable headless mode.

browser = webdriver.Firefox(
    firefox_binary=firefox_bin, capabilities=capabilities, options=options)

print('opening the page', browser)
browser.get("https://instagram.com/thelonetuga/")
html = browser.page_source

browser.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
numberPosts = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/a/span').text
numberFollowers = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text

new_page = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a').get_attribute('href')
#browser.close()

browser.get(new_page)
numberLikesLastPhoto = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[2]/div/div/a/span').text

browser.close()

print("Number of Followers: "+numberFollowers)
print("Number of Posts: "+numberPosts)

print("Number of Likes last photo: "+numberLikesLastPhoto)

