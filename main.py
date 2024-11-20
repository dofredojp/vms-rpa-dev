from services.rpa_service.webdriver_service import WebDriverService
from util.logger import logger

class RPAController:
    def __init__(self):
        self.url = "https://10.68.202.204/bus/bus_webtool/"
        self.wb = WebDriverService()

    def initialize_webtool(self):
        #driver = WebDriverService()
        self.wb.open_to_chrome(self.url)

if __name__ == '__main__':
    rpa = RPAController()
    
    rpa.initialize_webtool()