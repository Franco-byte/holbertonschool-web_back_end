#!/usr/bin/env python3
'''
NoSQL Basiscs
'''

def list_all(mongo_collection) -> list:
    '''
    List all
    '''
    doc = []
    for _ in mongo_collection.find():
        doc.append(_)
    return doc
