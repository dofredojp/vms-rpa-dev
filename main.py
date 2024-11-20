from services.rpa_service.webdriver_service import WebDriverService
from services.rpa_service.login_service import LoginService
from selenium.webdriver.support import expected_conditions as EC
from services.vms_service.voucher_code_files_service import VoucherCodeFileService
from selenium.webdriver.common.by import By
import time
from util.logger import logger

class RPAController:

    #Constructor, to initialize the webdriver and services
    def __init__(self):
        self.url = "https://10.68.202.204/bus/bus_webtool/"
        self.wb = WebDriverService()
        self.login_service = LoginService(self.wb)
        self.voucher_code_file_service = VoucherCodeFileService(self.wb)

    #Function to open browser > redirect > authentication 
    def initialize_webtool(self):
        self.wb.open_to_chrome(self.url)
        self.login_service.login()
        
    def process_transaction(self):
        logger.info("Kindly wait 5 minutes for voucher to reflect.")
        time.sleep(5)
        self.voucher_code_file_service.check_error_code()


if __name__ == '__main__':
    
    #instantiate RPA controller
    rpa = RPAController()
    
    #start RPA process
    rpa.initialize_webtool()
    rpa.process_transaction()