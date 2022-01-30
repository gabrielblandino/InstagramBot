from time import time
from selenium import webdriver
import time

navegador = webdriver.Chrome("chromedriver.exe")


# Part 1 -> Login to instagram website
navegador.get("https://www.instagram.com/")
time.sleep(2)

# Part 2 -> Login with username and password
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("user")
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("password")
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(3)

# Part 3 -> Click on "Not now" of login informations
navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(2)

# Part 4 -> Click on "Not now" of nofitifications
navegador.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
time.sleep(1)

# Part 5 -> Click on he search bar
navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div/span').click()
time.sleep(0.5)

# Part 6 -> Enter thename of the profile you want
navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys("profile")
time.sleep(1)

# Part 7 -> Click on the desired profile
navegador.find_element_by_class_name('-qQT3').click()
time.sleep(5)

# Part 8 -> Follow the profile
navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button').click()
