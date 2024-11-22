import os
from dotenv import load_dotenv

from repository.appsheet import AppsheetAPI
import sys


class RRTService:
    def __init__(self):
        self.appsheet_api = AppsheetAPI()

    def update_status(self, transaction_id, status, remarks):
        self.appsheet_api.update_row(transaction_id = transaction_id, status = status, remarks = remarks)