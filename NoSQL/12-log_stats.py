#!/usr/bin/env python3
"""
Log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count()
    print("{} logs".format(total_logs))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check = nginx_collection.count({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))
