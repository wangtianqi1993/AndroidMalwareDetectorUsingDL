#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

from flask import Flask

from detector.config import APP_NAME
from detector.logger import DetectorLogger
from detector.web.util import ApplicationDetector

project_path = os.path.dirname(__file__)
sys.path.append(project_path)

app = Flask(__name__, static_path='/static')


# 全局的logger
logger = DetectorLogger()
detector = ApplicationDetector

# import all route here
from . import index


@app.before_first_request
def service_init():
    logger.info('[%s]service starting.....' % APP_NAME)


def main():
    app.run(host='0.0.0.0', port=1234, debug=True)


if __name__ == '__main__':
    main()
