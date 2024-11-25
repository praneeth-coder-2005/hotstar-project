from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Auto-download the correct ChromeDriver version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open Hotstar
    print("Opening Hotstar...")
    driver.get("https://www.hotstar.com/in")

    # Wait for manual login
    print("Please log in to your Hotstar account manually. You have 60 seconds.")
    time.sleep(60)

    # Fetch cookies
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
