from selenium.webdriver.common.by import By
from services.rpa_service.webdriver_service import WebDriverService
from util.logger import logger

class LoginService:
    def __init__(self, wb):
        self.wb = wb
    
    def login(self):
        #for testonly
        logger.info("Logging in...")
        username = self.wb.chrome_driver.find_element(By.ID, "txt_uname")
        username.send_keys("ms244013")
        password = self.wb.chrome_driver.find_element(By.ID, "txt_passwd")
        password.send_keys("Jo123jo45!")
        self.wb.chrome_driver.find_element(By.ID, "login-button").click()
        logger.info("Login Success!")
        self.wb.chrome_driver.get("https://10.68.202.204/bus/bus_webtool/index.php?mod=vms_voucher_code_files&op=upload")

    def logout(self):
        logger.info("Logging out from the webtool")
        logout_element = self.wb.chrome_driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        logout_element.click()
        logger.info("Logged out successfully")
        self.wb.chrome_driver.quit()
        logger.info("Webtool closed")