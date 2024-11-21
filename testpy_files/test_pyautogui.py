import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

def locate_file(folder_path, target_file_prefix):

    for file in os.listdir(folder_path):
        if file.startswith(target_file_prefix):
            return os.path.join(folder_path, file)
    return None


def upload_file_via_browser(file_path):

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors') # To bypass the unsecure message
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


    try:
        # Open the login page
        driver.get("https://10.68.202.204/bus/bus_webtool/login.php")

        # Locate the username and password fields
        username_field = driver.find_element(By.ID, "txt_uname")
        password_field = driver.find_element(By.ID, "txt_passwd")

        # Enter credentials
        username_field.send_keys("ms244011")
        password_field.send_keys("")
        driver.find_element(By.ID, "login-button").click()

        driver.get("https://10.68.202.204/bus/bus_webtool/index.php?mod=vms_voucher_code_files&op=upload")
        time.sleep(2)

        # Locate the file input element and send the file path directly
        upload_button = driver.find_element(By.NAME, "file")
        upload_button.send_keys(file_path)  # Send the file path directly
        time.sleep(2)

        # Submit the form
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()
        time.sleep(3)

        # Wait for the success message to appear
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success' and text()='Succesfully uploaded file.']"))
        )
        print("Message found:", success_message.text)
        print("File Path: ", file_path)

        # Variables
        uploaded_filename = "vms_vouchercodes_grabtm.20240821.150000.csv.asc"  # Put filename here
        today = datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        # Fill out the "Filename" field
        # filename_field = driver.find_element(By.ID, "txt_filename")
        # filename_field.send_keys("vms_vouchercodes_grabtm.20240821.150000.csv.asc")

        # # Fill out the "Date Uploaded From" field
        # date_from_field = driver.find_element(By.ID, "txt_upload_date_from")
        # date_from_field.clear()  # Clear any pre-filled value
        # date_from_field.send_keys(yesterday)

        # # Fill out the "Date Uploaded To" field
        # date_to_field = driver.find_element(By.ID, "txt_upload_date_to")
        # date_to_field.clear()  # Clear any pre-filled value
        # date_to_field.send_keys(today)

        # PUT FOR LOOP HERE TO CHECK THE ERROR DESCRIPTION 

        # print("FILE HAS BEEN UPLOADED SUCCESSFULL WITHOUT ISSUES!")

    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to close the browser...")  

    input("Press Enter to close the browser...")  


def main():
    folder_path = "C:/Users/josemari.masangkay_g/Downloads"  # Path to the folder containing the target file
    target_file_prefix = "vms_vouchercodes"

    # Locate the target file
    file_path = locate_file(folder_path, target_file_prefix)
    if not file_path:
        print(f"Error: File '{target_file_prefix}' not found in folder '{folder_path}'.")
        return

    upload_file_via_browser(file_path)

if __name__ == "__main__":
    main()
