'''
FB MESSAGE BOT
Developed by Vichitr Gandas
Date: 04 June 2018
Language: Python
API: Selenium WebDriver
'''

#import the modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import [TheNameOfTheExceptionClass]
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep 

#data
URL_TO_FB='https://www.facebook.com/'
USERNAME='YOUR EMAIL/PHONE'
PASSWORD='YOUR PASSWORD'
FRIEND='YOUR FRIEND NAME'
MESSAGE="Hi! I'm a Bot created by vichitr Gandas. :)"

#Open the url
browser = webdriver.Chrome()
browser.get(URL_TO_FB)
sleep(1)

#enter username and password then click login
username=browser.find_element_by_xpath("//input[@id='email']")
username.send_keys(USERNAME)
password=browser.find_element_by_xpath("//input[@id='pass']")
password.send_keys(PASSWORD)
login = browser.find_element_by_xpath("//input[@value='Log In']")
login.click()
sleep(1)

#open message box
message_box = browser.find_element_by_xpath("//a[@class='jewelButton _3eo8']")
browser.execute_script("arguments[0].click();",message_box)
sleep(1)

#select the user to send messages
friend_url = "//*[text()='"+FRIEND+"']"
friend = browser.find_element_by_xpath(friend_url)
browser.execute_script("arguments[0].click();",friend)
sleep(1)

#send the message
message = browser.find_element_by_xpath("//div[@class='notranslate _5rpu']")
message.send_keys(MESSAGE)
message.send_keys(Keys.ENTER)
sleep(1)

#close the browser
browser.close()
