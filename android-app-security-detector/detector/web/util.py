#!/usr/bin/python
# -*- coding: utf-8 -*-

from androguard.core.bytecodes import apk
from androguard.core import androconf

from detector.ad.core import check_adware_from_config
from detector.config import DECOMPRESS_PATH
from detector.constants import DetectorMode
from detector.h5.util import DecompressApk
from detector.h5.util import H5Detector


class ApplicationDetector(object):
    def __init__(self):
        self.de_apk = DecompressApk()
        self.h5_detector = H5Detector()

    def _check_application_h5(self, application):
        out_path = self.de_apk.decompress(application, DECOMPRESS_PATH)
        if self.de_apk.checker(out_path, mode=DetectorMode.js):
            return True
        else:
            return False

    def check_application_h5(self, application):
        return self._check_application_h5(application)

    def _check_application_advertisement(self, application):
        ret_type = androconf.is_android(application)

        if ret_type == "APK":
            try:
                a = apk.APK(application)
                if a.is_valid_APK():
                    return check_adware_from_config(a)
                else:
                    return False
            except Exception, e:
                print(e.message)
        return False

    def check_application_advertisement(self, application):
        return self._check_application_advertisement(application)

    def _check_application_malware(self, application):
        pass

    def check_application_malware(self, application):
        return self._check_application_malware(application)
