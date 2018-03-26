# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

from Queue import Queue


class DetectorTask:
    def __init__(self):
        self.task_id = Queue(maxsize=0)
        self.app_name = Queue(maxsize=0)
        self.wed_ip = Queue(maxsize=0)
        self.sign = Queue(maxsize=0)
        self.port = Queue(maxsize=0)
        self.path = Queue(maxsize=0)

    def getsize(self):
        return self.task_id.qsize()

# Global Task Queue
detector_task = DetectorTask()
# running task
running_detector_task = dict()
