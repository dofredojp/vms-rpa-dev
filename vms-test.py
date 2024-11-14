from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--incognito')

# Set up WebDriver with the options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Open the login page
    driver.get("https://10.68.202.204/bus/bus_webtool/index.php?mod=vms_voucher_code_files")

    # Locate the username and password fields
    username_field = driver.find_element(By.ID, "txt_uname")
    password_field = driver.find_element(By.ID, "txt_passwd")

    # Enter credentials
    username_field.send_keys("ms244011")
    password_field.send_keys("Dofredo1996$$")
    driver.find_element(By.ID, "login-button").click()

    driver.get("https://10.68.202.204/bus/bus_webtool/index.php?mod=vms_voucher_code_files")

    # elements = driver.find_elements(By.XPATH, "//a[@class='dropdown-toggle']")
    # for element in elements:
    #     if element.text == "VMS":
    #         print("FOUND!")
    #         element.click()

    # voucher_code_files_link = driver.find_element(By.XPATH, "//a[contains(@href, 'index.php?mod=vms_voucher_code_files') and text()='Voucher Code Files']")
    # print(voucher_code_files_link.text)
    # voucher_code_files_link.click()

except Exception as e:
    print(f"An error occurred: {e}")
    input("Press Enter to close the browser...")  

# finally:
#     driver.quit()

# halt browser
input("Press Enter to close the browser...")  

