"""
NOTE SCRIPT DOESN'T IMPLEMENT CAPTCHA SOLVING
(But script waits 30s for user to solve it before timeout)

This is a script to collect daily rewards on AWS Emerging Talent.

This script uses Selenium to automate the process of logging in to the AWS Emerging Talent website,
claiming the daily reward, and printing a success message.
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

PATH = "/usr/bin/chromedriver"

cService = webdriver.ChromeService(executable_path=PATH)

driver = webdriver.Chrome(service=cService)

driver.get("https://aws-emergingtalent.influitive.com/")
DELAY = 30 # seconds
try:
    login = WebDriverWait(driver, DELAY).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Log In'))
    )
    login.click()
    username = WebDriverWait(driver, DELAY).until(
        EC.presence_of_element_located((By.ID, 'user_email'))
    )
    # TODO
    # Replace the asterisks with your email and password
    username.send_keys("*************@gmail.com")
    password = driver.find_element(By.ID, "user_password")
    password.send_keys("************")
    signin = driver.find_element(By.ID, "sign-in-button")
    signin.click()
except TimeoutException:
    print("User login took too much time!")

try:
    claim = WebDriverWait(driver, DELAY).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'css-10meywq'))
    )
    claim.click()
    print("Successfully claimed daily reward!")
except TimeoutException:
    print ("Claiming took too much time!")
