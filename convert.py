from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import json
import time

# Configure Firefox options
firefox_options = Options()
firefox_options.add_argument("--start-maximized")  # Start browser maximized
firefox_options.add_argument("--no-sandbox")  # For VPS environments
firefox_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues

# Initialize WebDriver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

try:
    # Open the website
    driver.get("https://www.hotstar.com/in")  # Replace with your URL
    print("Please log in manually...")

    # Allow time for manual login
    time.sleep(60)  # Wait for user to log in (adjust if necessary)

    # Save cookies to a file
    cookies = driver.get_cookies()
    with open("cookies_firefox.json", "w") as file:
        json.dump(cookies, file)

    print("Cookies have been saved to 'cookies_firefox.json'.")

finally:
    # Close the browser
    driver.quit()
