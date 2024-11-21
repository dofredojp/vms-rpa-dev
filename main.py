from services.rpa_service.webdriver_service import WebDriverService
from services.rpa_service.login_service import LoginService
from services.rpa_service.menu_service import MenuService
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
        self.menu_service = MenuService(self.wb)
        self.login_service = LoginService(self.wb)
        self.voucher_code_file_service = VoucherCodeFileService(self.wb)

    #Function of open browser > redirect to url > authentication > redirect to vms upload
    def initialize_webtool(self):
        self.wb.open_to_chrome(self.url)
        self.login_service.login()
        self.menu_service.confirm_navigate_page()
    
    #Function of verifying existing voucher code > fetching file > upload file > check for error code
    def process_transactions(self):
        self.voucher_code_file_service.verify_existing_voucher()
        self.voucher_code_file_service.fetch_file()
        file_path = self.voucher_code_file_service.locate_file()
        self.voucher_code_file_service.upload_file_via_browser(file_path)
        logger.info("Kindly wait 5 minutes for voucher to reflect.")
        
        #Sleep for 5mins. for voucher to reflect
        #Set 3 seconds for testing only.
        time.sleep(3)
        self.voucher_code_file_service.check_error_code()
    
    #Function of logout to webtool > quit driver and close browser > delete voucher file in local user dir
    def close_app(self):
        self.login_service.logout()
        self.voucher_code_file_service.delete_voucher_file()

if __name__ == '__main__':
    
    #instantiate RPA controller
    rpa = RPAController()
    
    #start RPA process
    rpa.initialize_webtool()
    rpa.process_transactions()
    rpa.close_app()