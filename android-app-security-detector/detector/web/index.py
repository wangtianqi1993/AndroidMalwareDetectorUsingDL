#!/usr/bin/python
# -*- coding: utf-8 -*-

from detector.web import app
from detector.web import detector
from detector.web import logger
from detector.web.response import wrapper_response_success
from detector.web.response import wrapper_response_500


@app.route('/api/h5ware/<app_path>', methods=('GET',))
def check_app_adware(app_path):
    try:
        result = detector.check_application_h5(app_path)
        return wrapper_response_success(result)
    except Exception, e:
        logger.error(e.message)
        return wrapper_response_500({'exception_message': e.message})


@app.route('/api/adware/<app_path>', methods=('GET',))
def check_app_adware(app_path):
    try:
        result = detector.check_application_advertisement(app_path)
        return wrapper_response_success(result)
    except Exception, e:
        logger.error(e.message)
        return wrapper_response_500({'exception_message': e.message})


@app.route('/api/malware_test/<app_path>', methods=('GET',))
def check_app_adware(app_path):
    try:
        result = detector.check_application_malware(app_path)
        return wrapper_response_success(result)
    except Exception, e:
        logger.error(e.message)
        return wrapper_response_500({'exception_message': e.message})
