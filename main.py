from lib2to3.pgen2 import driver

from selenium import webdriver
from time import sleep

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import urllib.request

from selenium.webdriver.firefox.options import Options

page = urllib.request.urlopen("https://www.10minutemail.be/")
text = page.read().decode("utf8")
where = text.find("email2")
start_of_email = where + 8
end_of_email = start_of_email + 24
bemail = text[start_of_email:end_of_email]
print(bemail)
firefox_options = Options()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=firefox_options, executable_path='/usr/lib64/firefox/firefox')
binary = FirefoxBinary("/usr/lib64/firefox/firefox")

driver.get("https://twitter.com/signup")
print("Twitter Opened")
sleep(2)

user_name = driver.find_element_by_id("full-name")
user_name.send_keys("abinav kumar")
print("name set for bot")
sleep(1)

user_email = driver.find_element_by_id("email")
user_email.send_keys(bemail)
print("email set")

user_password = driver.find_element_by_id("password")
user_email.send_keys("199c1997D")
print("password done")

submit = driver.find_element_by_id("submit_button")
submit.click()

print("Twitter Logged ")

