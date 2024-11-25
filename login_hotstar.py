from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Paths to Chrome and ChromeDriver
chrome_binary_path = "/usr/bin/google-chrome"  # Google Chrome binary path
chromedriver_path = "/usr/local/bin/chromedriver"  # ChromeDriver binary path

# Set up Chrome options
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary_path
options.add_argument("--start-maximized")  # Start the browser maximized
options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection

# Initialize WebDriver
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open Hotstar
    print("Opening Hotstar...")
    driver.get("https://www.hotstar.com/in")

    # Wait for manual login
    print("Please log in to your Hotstar account manually. You have 60 seconds.")
    time.sleep(60)  # Adjust if more time is needed

    # Fetch cookies after login
    cookies = driver.get_cookies()
    print("Cookies fetched successfully!")

    # Save cookies to a file
    with open("hotstar_cookies.txt", "w") as file:
        for cookie in cookies:
            file.write(f"{cookie}\n")
    print("Cookies saved to 'hotstar_cookies.txt'.")

finally:
    # Close the browser
    print("Closing the browser...")
    driver.quit()
