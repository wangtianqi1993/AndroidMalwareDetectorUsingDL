#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

from bson.objectid import ObjectId
from pymongo import MongoClient
import pymongo
from detector.config import MONGODB_HOST
from detector.config import MONGODB_PORT
from detector.config import DETECTOR_DB_NAME
from detector.config import PERMISSIONS_COLLECTION
from detector.db.util import get_permissions_from_google


client = MongoClient(MONGODB_HOST, MONGODB_PORT)


class MongDBSession(object):
    def __init__(self, db_name=DETECTOR_DB_NAME):
        self.session = client
        self.new_db = None

        # init
        self._connect_db(db_name)
        self.collection = None

    def create_db(self, db_name=DETECTOR_DB_NAME):
        self.new_db = self.session[db_name]

    def _connect_db(self, db_name=DETECTOR_DB_NAME):
        self.connect = self.session[db_name]

    def _connect_collection(self, collection):
        self.collection = self.connect[collection]

    def query_all(self, collection, find_=None):
        self._connect_collection(collection)
        return self.collection.find(find_)

    def query_one(self, collection, find_=None):
        self._connect_collection(collection)
        return self.collection.find_one(find_)

    def query_sort(self, collection, sort, find_=None, limit=1):
        self._connect_collection(collection)
        results = self.collection.find(find_).sort(
            sort, pymongo.DESCENDING).limit(limit)

        if limit == 1:
            return results[0]

        return results

    def query_by_id(self, collection, query_id):
        self._connect_collection(collection)
        return self.collection.find_one({'_id': ObjectId(query_id)})

    def insert_one(self, collection, value):
        self._connect_collection(collection)
        inserted_id = self.collection.insert_one(value).inserted_id
        return inserted_id

    def insert_all(self, collection, values):
        self._connect_collection(collection)
        inserted_ids = self.collection.insert_many(values).inserted_ids
        return inserted_ids


class PermissionSession(MongDBSession):
    def __init__(self, db_name=DETECTOR_DB_NAME):
        super(PermissionSession, self).__init__(db_name=db_name)


if __name__ == '__main__':
    session = PermissionSession()
    permissions = get_permissions_from_google()

    post_permissions = {
        'permissions': permissions,
        'createdAt': datetime.now()
    }

    print session.insert_one(PERMISSIONS_COLLECTION, post_permissions)

