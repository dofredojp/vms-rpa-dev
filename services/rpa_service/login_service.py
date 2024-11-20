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
        self.wb.chrome_driver.get("https://10.68.202.204/bus/bus_webtool/index.php?mod=vms_voucher_code_files")

    #def logout(self)