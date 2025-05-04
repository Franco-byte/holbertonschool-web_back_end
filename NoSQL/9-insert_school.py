#!/usr/bin/env python3
'''
NoSQL Basiscs
'''


def insert_school(mongo_collection, **kwargs):
    '''Insert a new document in the collection'''
    return mongo_collection.insert_one(kwargs).inserted_id
