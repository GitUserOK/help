import selenium
from selenium import webdriver
from time import sleep

d = webdriver.Firefox()
d.get("https://www.google.com/gmail/about/")
sleep(5)
print("Done")
d.quit()
