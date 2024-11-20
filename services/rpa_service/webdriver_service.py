from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from RPA.Browser.Selenium import Selenium

class WebDriverService(Selenium):
    def __init__(self):
        print("Initializing Web Driver")
        #super().__init__(auto_close=auto_close_browser)
        self.actions = None
        self.__create_driver()

    def __create_driver(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_argument("--no-sandbox")
            options.add_argument("--ignore-ssl-errors=yes")
            options.add_argument("--ignore-certificate-errors")
            #options.add_argument("--headless")
            options.add_argument("--start-maximized")
            #options.add_argument("--window-size=1920,1080")
            self.chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        except Exception as e:
            print("Failed to create chrome driver. Ensure that it is installed properly.")
    
    def open_to_chrome(self, url):
        self.chrome_driver.get(url)
        self.chrome_driver.implicitly_wait("5")