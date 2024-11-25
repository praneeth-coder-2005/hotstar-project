from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Specify paths
chrome_binary_path = "/usr/bin/google-chrome"  # Path to your Chrome binary
chromedriver_path = "/usr/local/bin/chromedriver"  # Path to your ChromeDriver

# Set up Chrome options
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary_path
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection

# Initialize WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open Hotstar website
driver.get("https://www.hotstar.com/in")

# Wait for manual login
print("Please log in to your Hotstar account manually.")
time.sleep(60)  # Adjust the sleep duration as needed

# Fetch cookies after login
cookies = driver.get_cookies()
print("Cookies fetched:")
for cookie in cookies:
    print(cookie)

# Save cookies to a file
with open("hotstar_cookies.txt", "w") as file:
    for cookie in cookies:
        file.write(f"{cookie}\n")

# Close the browser
driver.quit()
