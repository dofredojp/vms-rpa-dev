from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (NoSuchElementException,TimeoutException)
import time
from util.logger import logger

class MenuService:
    def __init__(self, wb):
        self.expected_title = "VMS Voucher Code Files, Upload"
        self.wb = wb

    def confirm_navigate_page(self):
        try:
            logger.debug("Verifying Page..")
            # Web driver wait until element to be visible
            WebDriverWait(self.wb.chrome_driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "pagetitle"))
            )

            actual_title = self.wb.chrome_driver.find_element(By.CLASS_NAME, "pagetitle").text
            assert actual_title == self.expected_title

        except NoSuchElementException as e:
            raise f"Navigate to Message Page Encountered issues: {e}"

        except TimeoutException as e:
            raise (f"Navigate to Page Encountered issues: Page timeout! "
                   f"Error message: {e}")

        except AssertionError as e:
            raise (f"Navigate to Message Patterns Page Encountered issues: Page not found! "
                   f"Error message: {e}")
        else:
            logger.info(f"Navigation Successful")
            return True
            