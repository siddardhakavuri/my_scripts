"""
NOTE SCRIPT DOESN'T IMPLEMENT CAPTCHA SOLVING
(But script waits 30s for user to solve it before timeout)

This is a script to collect daily rewards on AWS Emerging Talent.

This script uses Selenium to automate the process of logging in to the AWS Emerging Talent website,
claiming the daily reward, and printing a success message.
"""
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def reward_collector():
    """
        Returns:
        error code 1 if the script times out
    """
    path = "/usr/bin/chromedriver"

    cService = webdriver.ChromeService(executable_path=path)

    driver = webdriver.Chrome(service=cService)

    driver.get("https://aws-emergingtalent.influitive.com/")
    delay = 30 # seconds
    try:
        login = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Log In'))
        )
        login.click()
        username = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, 'user_email'))
        )

        # Replace the asterisks with your email and password
        username.send_keys("************")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("************")
        signin = driver.find_element(By.ID, "sign-in-button")
        signin.click()
    except TimeoutException:
        print("User login took too much time!")

    try:
        button = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((
            By.CLASS_NAME, 'css-10meywq')))
        button.click()
        print("Successfully claimed daily reward!")
    except TimeoutException:
        print ("Claiming took too much time!")
        sys.exit(1)

reward_collector()
