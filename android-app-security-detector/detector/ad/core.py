# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
from datetime import datetime
from androguard.core import androconf
from androguard.core.bytecodes import apk
import numpy
from numpy import zeros
from sklearn.naive_bayes import *
from sklearn import svm
from sklearn.externals import joblib
from detector.config import *
from detector.db.session import MongDBSession
from detector.logger import AdDetectorLogger

logger = AdDetectorLogger()


def check_adware_from_config(real_filename, config=AD_FEATURE_FILE):
    """
    Check app is adware from ad feature db.
    :param apk: the path of checking app
    :param config: adware feature db
    :return: True or False
    """
    ret_type = androconf.is_android(real_filename)
    if ret_type == "APK":
        logger.info(os.path.basename(real_filename) + ':')
        try:
            a = apk.APK(real_filename)
            if a.is_valid_APK():
                with open(config, 'r') as f:
                    js = json.loads(f.read())

                    # 到apk的配置文件中取出申明的activity名字
                    activities = a.get_activities()
                    for i in activities:
                        # logger.info(i)
                        if i in js[0].keys():
                            logger.info("yes!")
                            ad_name = js[0][i]
                            return ad_name

                        for j in js[0].keys():
                            pattern = re.compile(j)
                            if pattern.match(i):
                                logger.info("yes!")
                                ad_name = js[0][j]
                                return ad_name

                    services = a.get_services()
                    for i in services:
                        # logger.info(i)
                        if i in js[0].keys():
                            logger.info("yes!")
                            ad_name = js[0][i]
                            return ad_name

                        for j in js[0].keys():
                            pattern = re.compile(j)
                            if pattern.match(i):
                                logger.info("yes!")
                                ad_name = js[0][j]
                                return ad_name

                    receivers = a.get_receivers()
                    for i in receivers:
                        # logger.info(i)
                        if i in js[0].keys():
                            logger.info("yes!")
                            ad_name = js[0][i]
                            return ad_name
                        for j in js[0].keys():
                            pattern = re.compile(j)
                            if pattern.match(i):
                                logger.info("yes!")
                                ad_name = js[0][j]
                                return ad_name
            else:
                logger.info("INVALID")
        except Exception, e:
            logger.info('error in check_adware_from_config model')
            logger.info(e)

    return False

