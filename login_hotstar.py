from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Step 1: Open the direct login page
    driver.get("https://www.hotstar.com/in/mypage#mp-login")
    print("Navigated to Hotstar login page.")
    time.sleep(5)  # Allow page to load

    # Step 2: Click the Login button
    try:
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))  # Update selector if needed
        )
        login_button.click()
        print("Clicked Login button.")
    except Exception as e:
        print("Error locating or clicking the Login button:", e)
        raise

    # Step 3: Wait for the mobile number input field
    try:
        mobile_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "mobileNumber"))  # Update ID if incorrect
        )
        mobile_input.send_keys(MOBILE_NUMBER)
        print("Entered mobile number.")
    except Exception as e:
        print("Error locating or interacting with the mobile number input field:", e)
        raise

    # Step 4: Submit mobile number
    try:
        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'CONTINUE')]"))
        )
        continue_button.click()
        print("Submitted mobile number. Waiting for OTP...")
    except Exception as e:
        print("Error locating or interacting with the 'CONTINUE' button:", e)
        raise

    time.sleep(5)  # Wait for OTP request

    # Step 5: Pause for manual OTP entry
    print("Waiting for you to manually enter the OTP in the browser...")
    time.sleep(30)  # Allow time for manual OTP entry

    # Step 6: Save cookies after login
    cookies = driver.get_cookies()
    with open("hotstar_cookies.json", "w") as file:
        json.dump(cookies, file)

    print("Login successful! Cookies saved to 'hotstar_cookies.json'.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    driver.quit()
