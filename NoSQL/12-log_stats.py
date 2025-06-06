#!/usr/bin/env python3
'''
NoSQL Basics
'''


from pymongo import MongoClient


def log_stats():
    '''
    Function documented
    '''
    client = MongoClient()
    database = client.logs
    collection = database.nginx
    x = collection.count_documents({})
    print(f"{x} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{status_count} status check")

if __name__ == "__main__":
    log_stats()