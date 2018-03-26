# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

from androguard.core import androconf
from androguard.core.bytecodes import apk
from sklearn.naive_bayes import *
from detector.ad.core import check_adware_from_config

from detector.ad.permission.train import AdClassifierTrain

from detector.logger import AdDetectorLogger
from detector.config import *


logger = AdDetectorLogger()
train_classifier = AdClassifierTrain()


def _use_check_ad():
    for root, dirs, files in os.walk(TRAIN_APK_PATH, followlinks=True):
        if files:
            for f in files:
                real_filename = root
                if real_filename[-1] != "/":
                    real_filename += "/"
                real_filename += f
                ret_type = androconf.is_android(real_filename)
                if ret_type == "APK":
                    logger.info(os.path.basename(real_filename) + ':')
                    try:
                        a = apk.APK(real_filename)
                        if a.is_valid_APK():
                            check_adware_from_config(a)
                        else:
                            logger.info("INVALID")
                    except Exception, e:
                        logger.info(e)
        else:
            logger.error("directory not exits!!!")


