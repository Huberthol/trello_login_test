from login_data_base import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Chrome
driver = webdriver.Chrome()

# Data base login and password
dane_logowania = login_data_base

# Open text file in write mode
with open("wyniki.txt", "w") as file:
# Loop
    for dane in dane_logowania:
        # Open page
        driver.get("https://trello.com/login")

        # Find login and send login keys
        driver.find_element(By.CSS_SELECTOR, '#user').send_keys(dane["login"])

        # Click login button
        driver.find_element(By.CSS_SELECTOR, '#login').click()

        # Wait for the password form
        driver.implicitly_wait(3)
        # Find password and send password keys
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys(dane["haslo"])

        # Find login button and click
        driver.find_element(By.CSS_SELECTOR, "#login").click()

        time.sleep(2)

        # If you are on the url adres with "boards" you are on the correct site
        if "boards" in driver.current_url:
            result = f"Login: {dane['login']}, password: {dane['haslo']} - correct."
        else:
            result = f"Login: {dane['login']}, password: {dane['haslo']} - wrong."

        # Save data in text file
        file.write(result + "\n")

        # Print results in consol
        print(result)

        time.sleep(1)

# Close browser
driver.quit()


