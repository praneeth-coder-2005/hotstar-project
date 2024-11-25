from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

# Your mobile number
MOBILE_NUMBER = 'your-mobile-number'

# Initialize Chrome in headless mode for VPS
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Enable headless mode for VPS
options.add_argument("--no-sandbox")  # Required for running as root
options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory issues

# Automatically download and use the correct ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Step 1: Open Hotstar
    driver.get("https://www.hotstar.com/in")
    time.sleep(5)  # Wait for the page to load

    # Step 2: Click the login button
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'LOGIN')]")
    login_button.click()
    time.sleep(2)  # Wait for the login modal to appear

    # Step 3: Enter mobile number
    mobile_input = driver.find_element(By.ID, "mobileNumber")  # Update ID based on Hotstar's current DOM
    mobile_input.send_keys(MOBILE_NUMBER)

    # Step 4: Submit mobile number
    continue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'CONTINUE')]")
    continue_button.click()
    time.sleep(5)  # Wait for OTP to be sent

    # Step 5: Pause for manual OTP entry
    print("Waiting for you to manually enter the OTP in the browser...")
    time.sleep(30)  # Pause to allow OTP entry

    # Step 6: Save cookies after login
    cookies = driver.get_cookies()
    with open("hotstar_cookies.json", "w") as file:
        json.dump(cookies, file)

    print("Login successful! Cookies saved to 'hotstar_cookies.json'.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up and close the browser
    driver.quit()
