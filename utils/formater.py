# !/usr/bin/env python
# -*- coding:utf-8 -*-
# format.py

import os
import re
import xlrd
import codecs
import json
from utils import log
from config.config import sheet_name

class Formater():

    def __init__(self):

        self.logger = log.set_up_logger()

    def get(self, file_path):

        """get excel data"""
        try:
            data = xlrd.open_workbook(file_path)
            return data 
        except Exception as e:
            self.logger.error("get data failed, {}".format(e))
            return None
    
    def save(self, file_path, file_name, data):

        output = codecs.open(file_path + "/" + file_name + ".json", "w", "utf-8")
        output.write(data)
        output.close()

    def segment(self, data):

        return re.findall(r"\d+\.?\d*", data)



    def xls_to_json(self, file_path):

        book = self.get(file_path) if self.get(file_path) else None
        player_sheet = book.sheet_by_name(sheet_name)
        self.logger.debug("sheet_name is {}".format(player_sheet.name))
        row_0 = player_sheet.row(0)[0]
        self.logger.debug(row_0,type(row_0))
        merged_cells = player_sheet.merged_cells
        self.logger.debug("table.merged_cells:{}".format(player_sheet.merged_cells))

        for cell in merged_cells:
            result = {
                    "intro":{
                        "cn":"",
                        "en":""
                        },
                    "line":{
                        "cn":"",
                        "en":""
                        },
                    "players":None,
                    "record":[]
                    }
            datas = []
            for row in range(cell[0], cell[1]):
                kda = self.segment(str(player_sheet.row_values(row)[5]))
                player_id = int(player_sheet.row_values(row)[13])
                data = {
                        "name":str(player_sheet.row_values(row)[1]),
                        "cn":"",
                        "en":"",
                        "num":[],
                        "data":{
                            "kda": float(kda[0]),
                            "kills":float(kda[1]),
                            "deaths":float(kda[2]),
                            "assists":float(kda[3]),
                            "avg_gpm":float(player_sheet.row_values(row)[8]),
                            "avg_output":float(player_sheet.row_values(row)[9]),
                            "avg_harmed":float(player_sheet.row_values(row)[11]),
                            "avg_last_hit":float(player_sheet.row_values(row)[7])
                            }
                        }
                combined_data = {
                    player_id : data
                    }
                datas.append(combined_data)
            result["players"] = datas
            json_data = json.dumps(result, indent=4, sort_keys=True)
            self.logger.debug("json_data is {}".format(json_data))
            fpath = os.getcwd() + "/results/"
            
            self.save(fpath, str(int(player_sheet.row_values(cell[0])[0])), json_data)


                




                


#if __name__ == "__main__":
#   fmt = Formater()
#    fmt.xls_to_json("./20180918143111_S8.xlsx")
