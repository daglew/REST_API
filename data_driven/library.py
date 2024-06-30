import json
import jsonpath
import requests
import openpyxl


class Common:

    def __init__(self, file_name_path, sheet_name):
        global wk
        global sh
        wk = openpyxl.load_workbook(file_name_path)
        sh = wk[sheet_name]

    def fetch_row_count(self):
        rows = sh.max_row
        return rows



