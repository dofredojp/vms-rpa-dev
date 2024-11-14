from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver using webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Wait for the page to load
    # time.sleep(2)

    # Locate the username and password fields
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Enter test credentials
    username_field.send_keys("student")
    password_field.send_keys("Password123")

    # Click the submit button
    driver.find_element(By.ID, "submit").click()

    # Wait a few seconds for the login to process
    time.sleep(1)

    # Check for a success message to confirm login
    success_message = driver.find_element(By.TAG_NAME, "h1").text
    print(success_message)
    if "Logged In Successfully" in success_message:
        print("Login test passed: Logged in successfully.")
    else:
        print("Login test failed: Success message not found.")
   
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()

# Keep the browser open until you manually close it
# input("Press Enter to close the browser...")  # This keeps the browser open

