from services.rpa_service.webdriver_service import WebDriverService
from util.logger import logger

class RPAController:
    def __init__(self):
        self.url = "https://10.68.202.204/bus/bus_webtool/"
        self.driver = WebDriverService()

    def initialize_webtool(self):
        self.driver.open_to_chrome(self.url)

if __name__ == '__main__':
    rpa = RPAController()
    
    rpa.initialize_webtool()