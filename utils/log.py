# !/usr/bin/env python
# -*- coding:utf-8 -*-
# log.py

import logging

def set_up_logger():

    logger = logging.getLogger(__name__)
    fmt = '[%(asctime)s] [%(levelname)s] [%(message)s] [--> %(pathname)s [%(funcName)s] [%(lineno)s] [%(process)d]]'
    logging.basicConfig(format=fmt, level=logging.DEBUG)
    return logger
