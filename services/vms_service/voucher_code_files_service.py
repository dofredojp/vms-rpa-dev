from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.logger import logger
import os
import sys
import json
from datetime import datetime, timedelta
import time

class VoucherCodeFileService:
    def __init__(self, wb):
        self.gdrive_url = ""
        self.folder_path = os.environ.get("USERPROFILE")+"\Downloads"
        self.target_file_prefix = "vms_vouchercodes"
        self.uploaded_filename = ""
        self.today = datetime.now().strftime("%m-%d-%Y")
        self.yesterday = (datetime.now() - timedelta(days=1)).strftime("%m-%d-%Y")
        self.wb = wb
    
    def fetch_file(self):
        # Read and Access json file
        test_json_file = 'test_data/json/test1.json'
        logger.info("Fetching file..")
        try:
            with open(test_json_file, 'r') as file:
                data = json.load(file)
            self.gdrive_url = data["create"][0]["voucherFileUrl"]
            self.wb.chrome_driver.get(self.gdrive_url)
            time.sleep(2)

        except FileNotFoundError:
            logger.info("The JSON file was not found.")
            sys.exit(1)
        except KeyError:
            logger.info("The key you are looking for doesn't exist.")
            sys.exit(1)
        except json.JSONDecodeError:
            logger.info("Error decoding the JSON file.")
            sys.exit(1)
            
    def locate_file(self):
        file_path_final = ""
        logger.info("Locationg file...")
        for file in os.listdir(self.folder_path):
            if file.startswith(self.target_file_prefix):
                #Get the filename
                self.uploaded_filename = file
                #Join path with filename
                file_path_final = os.path.join(self.folder_path, file)
                self.folder_path_final = file_path_final
                return file_path_final
            
        if not file_path_final:
            raise Exception(f"\nError: File '{self.target_file_prefix}' not found in folder '{self.folder_path}'.")

        return file_path_final

    def upload_file_via_browser(self, file_path):
        try:
            logger.info("File found! upload in progress..")
            # Locate the file input element and send the file path directly
            upload_button = self.wb.chrome_driver.find_element(By.NAME, "file")
            upload_button.send_keys(file_path)  # Send the file path directly
            time.sleep(2)

            # Submit the form
            submit_button = self.wb.chrome_driver.find_element(By.XPATH, "//input[@type='submit']")
            submit_button.click()
            time.sleep(3)

            # Wait for the success message to appear
            success_message = WebDriverWait(self.wb.chrome_driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success' and text()='Succesfully uploaded file.']"))
            )
            logger.info("Message found: " + success_message.text)
            logger.info("File Path: " + file_path)
        except Exception as e:
            logger.info("UPLOAD ERROR! make sure filename is in the format vms_vouchercodes_<PARTNER_NAME>.<YYYYMMDD>.<HHMMSS>.csv.asc")
            print(e)
            sys.exit(1)

    def apply_filter(self):
        logger.info("Applying filter to get vms voucher details")

        #Fill out the "Filename" field
        filename_field = self.wb.chrome_driver.find_element(By.ID, "txt_filename")
        #Remove '.asc' by getting total char length and subtract by 4
        getLength = len(self.uploaded_filename)
        filename_field.send_keys(self.uploaded_filename[0:getLength-4])

        # Fill out the "Date Uploaded From" field
        date_from_field = self.wb.chrome_driver.find_element(By.ID, "txt_upload_date_from")
        date_from_field.clear()  # Clear any pre-filled value
        date_from_field.send_keys(self.yesterday)

        # Fill out the "Date Uploaded To" field
        date_to_field = self.wb.chrome_driver.find_element(By.ID, "txt_upload_date_to")
        date_to_field.clear()  # Clear any pre-filled value
        date_to_field.send_keys(self.today)

        # Click Apply button
        apply_button = self.wb.chrome_driver.find_element(By.ID, "search3")
        apply_button.click()

    def check_error_code(self):
        
        self.apply_filter()

        #PUT FOR LOOP HERE TO CHECK THE ERROR DESCRIPTION 
        WebDriverWait(self.wb.chrome_driver, 5).until(
        EC.invisibility_of_element_located((By.ID, "col-empty")))

        #Get total max count of row in table
        row_count_total = len(self.wb.chrome_driver.find_elements(By.XPATH, "(//tbody)[3]//td[1]"))

        #option1-Check last row voucher error code (most recent uploaded voucher)
        get_error_code_text = self.wb.chrome_driver.find_element(By.XPATH, "(//td[4])[" + str(row_count_total) + "]").text
        #get_error_code_text = self.wb.chrome_driver.find_element(By.XPATH, "(//td[4])[1]").text
        get_error_code = int(get_error_code_text)
        get_error_message = self.wb.chrome_driver.find_element(By.XPATH, "(//td[5])[" + str(row_count_total) + "]").text
        
 
        if get_error_code > 2:
            #logger.info("FOUND ERROR CODE, SEE ERROR DESCRIPTION: " + get_error_message)
            raise Exception("\nERROR CODE: " + str(get_error_code) + "\nERROR DESCRIPTION: " + get_error_message)
            #self.wb.chrome_driver.quit()
            
        else: 
            logger.info("FILE HAS BEEN UPLOADED SUCCESSFULL WITHOUT ISSUES!")


        #option2-Check all each row error code in current page table (in progress)
        #for i in range(row_count_total):
        #   error_codes = self.wb.chrome_driver.find_elements(By.XPATH, "(//td[4])["+i+"]")
        #   if error_codes > 0: self.wb.chrome_driver.quit()

    def verify_existing_voucher(self):
            logger.info("Verifying if voucher code exist...")
            file_check = ""
            for file in os.listdir(self.folder_path):
                if file.startswith(self.target_file_prefix):
                    logger.info("Found existing voucher! '"+file+"' voucher has been deleted\n will proceed to vms upload")
                    file_check = file
                    os.remove(os.path.join(self.folder_path, file))
                    break
            if not file_check: logger.info("No voucher found, will proceed to vms upload")

    def delete_voucher_file(self):
        logger.info("Locating file to delete...")
        file_path = os.path.join(self.folder_path, self.uploaded_filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
                logger.info("Delete successful\n VMS VOUCHER CODE UPLOAD ENDED")
        except Exception as e:
            logger.info('Failed to delete %s. Reason: %s' % (file_path, e))
    