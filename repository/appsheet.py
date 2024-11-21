import requests
import json
import os
from util.logger import logger
from datetime import datetime

class AppsheetAPI:
    def __init__(self):
        self.url = os.getenv("APPSHEET_API_URL")
        self.headers = {
            'Content-Type': 'application/json'
        }

    def update_row(self, transaction_id, status, remarks):
        now = datetime.now()
        timestamp = now.strftime("%m/%d/Y, %H:%M:%S")
        logger.info(timestamp)

        payload = json.dumps({
            "Action": 'update',
            "Properties": {},
            "Rows": [
             {
                "status" : status,
                "rpaRemarks" : f'{remarks}',
                "timeStampDeployment": f'{timestamp}',
                "vmsImplemTemplateID": f'{transaction_id}'
            }
        ]
    })
        logger.info(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        logger.info(self.url)
        response = requests.request("PUT", self.url, headers=headers, data=payload)
        logger.info(f"AppSheet response {response}")
        return response