from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

# Configure WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode if needed
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

try:
    # Open Hotstar login page
    driver.get("https://www.hotstar.com/in")
    time.sleep(5)

    # Click on login
    login_button = driver.find_element(By.XPATH, '//button[contains(text(),"Sign In")]')
    login_button.click()
    time.sleep(2)

    # Enter mobile number
    phone_input = driver.find_element(By.XPATH, '//input[@type="tel"]')
    phone_number = "+917075049676"  # Replace with your mobile number
    phone_input.send_keys(phone_number)
    phone_input.send_keys(Keys.RETURN)
    time.sleep(2)

    # Wait for OTP input
    print("Enter the OTP manually on the browser...")
    time.sleep(60)  # Wait for manual OTP entry (adjust time as needed)

    # Extract cookies after login
    cookies = driver.get_cookies()
    with open("hotstar_cookies.json", "w") as f:
        json.dump(cookies, f, indent=4)

    print("Cookies saved to hotstar_cookies.json")

finally:
    driver.quit()
