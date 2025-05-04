#!/usr/bin/env python3
'''
NoSQL
'''


def schools_by_topic(mongo_collection, topic):
    '''Returns the list of school having a specific topic'''
    if mongo_collection is None:
        raise ValueError("mongo_collection cannot be None")
    if not isinstance(topic, str):
        raise ValueError("topic must be a string")
    return list(mongo_collection.find({"topics": topic}))
