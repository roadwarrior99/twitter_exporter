import json
import os
import sys
from openpyxl import Workbook
import argparse
import logging
from datetime import datetime
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def export(json_file_in, excel_file_out):
    #set up our excel workbook/worksheet

    if os.path.exists(json_file_in):
        start_of_load = datetime.now()
        logger.info(f"Loading json file {json_file_in}")
        twiter_data = json.load(open(json_file_in))
        logger.info(f"Loaded json file {json_file_in}")
        logger.info("Starting export")
        wb = Workbook()
        ws = wb.active
        ws.title = "data"
        ws["A1"] = "Date"
        ws["B1"] = "Tweet"
        row = 2
        for tweet in twiter_data:
            row_str = str(row)
            ws["A" + row_str] = tweet["date"]
            ws["B" + row_str] = tweet["tweet"]
            row += 1
        wb.save(excel_file_out)
    else:
        print(f"{json_file_in} doesn't exist")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='twiter_archive_to_excel',
                    description='Read the json archive file from twiter and export the data to an xlsx file.')
    parser.add_argument("--json-file-in", required=True, help="The json file you want to export from")
    parser.add_argument("--excel-file-out", required=True, help="The excel file you want save to")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    export(args.json_file_in, args.excel_file_out)
