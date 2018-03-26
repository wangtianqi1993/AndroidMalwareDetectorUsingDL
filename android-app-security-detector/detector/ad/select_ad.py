# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

import os
from androguard.core import androconf
from androguard.core.bytecodes import apk
from detector.logger import DetectorLogger
from core import check_adware_from_config


def select_not_found(apk_file):
    """
    select the not found apk_path which used ad feature
    :param apk_file:
    :return:
    """
    logger = DetectorLogger(path="not_checked_ad_logger.log")
    apklist = os.listdir(apk_file)
    not_check_sum = 0
    for apk_path in apklist:
        apk_path = os.path.join(apk_file, apk_path)
        if not check_adware_from_config(apk_path):

            ret_type = androconf.is_android(apk_path)
            if ret_type == "APK":

                try:
                    a = apk.APK(apk_path)
                    if a.is_valid_APK():
                        logger.info('//')
                        logger.info(os.path.basename(apk_path))
                        not_check_sum += 1
                        activities = a.get_activities()
                        services = a.get_services()
                        receivers = a.get_receivers()
                        for i in activities:
                            logger.info(i)
                        for i in services:
                            logger.info(i)
                        for i in receivers:
                            logger.info(i)
                    else:
                        logger.info("INVALID")
                except Exception, e:
                    logger.info(e)
    print not_check_sum
