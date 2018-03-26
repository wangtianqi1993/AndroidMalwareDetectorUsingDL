#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

from detector.config import TEST_NAIVEBAYES
from detector.config import TRAIN_NAIVEBAYES
from detector.config import TRAIN_PERMISSION
from detector.db.session import MongDBSession
from detector.config import BACKUP_TEST_PATH
from detector.config import BACKUP_TRAIN_PATH
from detector.config import BACKUP_BENIGN_SOURCE
from detector.config import BACKUP_MALWARE_SOURCE

def getdata_mongo(db_name, file_path):

    #backup mongodb of trainbayes
    session = MongDBSession()
    train_data = session.query_all(db_name)
    f = file(file_path, "w")
    for i in range(train_data.count()):
        for key in train_data[i]:
            f.write(key)
            f.write("\n")
            f.write(str(train_data[i][key]))
            f.write("\n")
        f.write("\n")
    f.close()


if __name__ == '__main__':
    getdata_mongo("malware_source", BACKUP_MALWARE_SOURCE)
