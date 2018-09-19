# !/usr/bin/env python
# -*- coding:utf-8 -*-
# convert.py

from utils.formater import Formater 
from config.config import sheet_name

fmt = Formater()
fmt.xls_to_json("./20180918190049_S8.xlsx")

