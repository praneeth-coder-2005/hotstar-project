from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Open Hotstar
driver.get("https://www.hotstar.com/in")

# Wait for user login
print("Please log in to your Hotstar account manually.")
time.sleep(60)  # Adjust time as needed for login

# Fetch Cookies
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
