from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

# Your mobile number
MOBILE_NUMBER = '+917075049676'

# Initialize Chrome in headless mode for VPS
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Enable headless mode for VPS
options.add_argument("--no-sandbox")  # Required for running as root
options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory issues

# Correctly initialize WebDriver using ChromeDriverManager
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)

try:
    # Step 1: Open the direct login page
    driver.get("https://www.hotstar.com/in/mypage#mp-login")
    print("Navigated to Hotstar login page.")
    time.sleep(5)  # Wait for the page to load

    # Step 2: Enter mobile number
    mobile_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "mobileNumber"))  # Adjust ID if incorrect
    )
    mobile_input.send_keys(MOBILE_NUMBER)
    print("Entered mobile number.")

    # Step 3: Submit mobile number
    continue_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'CONTINUE')]"))
    )
    continue_button.click()
    print("Submitted mobile number. Waiting for OTP...")
    time.sleep(5)  # Wait for OTP request

    # Step 4: Pause for manual OTP entry
    print("Waiting for you to manually enter the OTP in the browser...")
    time.sleep(30)  # Allow time for manual OTP entry

    # Step 5: Save cookies after login
    cookies = driver.get_cookies()
    with open("hotstar_cookies.json", "w") as file:
        json.dump(cookies, file)

    print("Login successful! Cookies saved to 'hotstar_cookies.json'.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
