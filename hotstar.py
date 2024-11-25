import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import subprocess

# Paths
chrome_binary_path = "/usr/bin/google-chrome"
chromedriver_path = "/usr/local/bin/chromedriver"
ffmpeg_output_path = "hotstar_live_recording.mp4"

# Set up Chrome options
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary_path
options.add_argument("--start-maximized")

# Initialize WebDriver
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Step 1: Open Hotstar and navigate to the live event
    driver.get("https://www.hotstar.com/in")
    print("Navigating to Hotstar...")
    time.sleep(5)

    # Log in if required
    try:
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        login_button.click()
        print("Please log in manually.")
        time.sleep(60)  # Adjust time as needed
    except Exception:
        print("Login not required or already logged in.")

    # Navigate to the live event URL
    live_event_url = "https://www.hotstar.com/in/sports/cricket/live-stream"
    driver.get(live_event_url)
    print("Opening live event...")
    time.sleep(10)

    # Step 2: Start screen recording with ffmpeg
    print("Starting screen recording...")
    ffmpeg_command = [
        "ffmpeg",
        "-y",  # Overwrite output file if it exists
        "-video_size", "1920x1080",  # Adjust based on your screen resolution
        "-framerate", "30",  # Frames per second
        "-f", "x11grab",  # Capture the screen
        "-i", ":0.0",  # Default display
        ffmpeg_output_path,
    ]
    ffmpeg_process = subprocess.Popen(ffmpeg_command)
    print("Recording in progress...")

    # Step 3: Record for a specified duration (e.g., 1 hour)
    record_duration = 60 * 60  # 1 hour
    time.sleep(record_duration)

    # Step 4: Stop recording
    print("Stopping recording...")
    ffmpeg_process.terminate()
    print(f"Recording saved as {ffmpeg_output_path}")

finally:
    # Close the browser
    print("Closing the browser...")
    driver.quit()
