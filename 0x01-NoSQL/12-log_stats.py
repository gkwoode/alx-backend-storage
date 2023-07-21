#!/usr/bin/env python3

# Write a Python script that provides some stats about Nginx logs stored in MongoDB:

import pymongo

def get_nginx_logs_stats(mongo_collection):
    total_logs = mongo_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_stats = {method: mongo_collection.count_documents({"method": method}) for method in methods}
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})

    return total_logs, methods_stats, status_check_count

if __name__ == "__main__":
    # Connect to the MongoDB server and the 'logs' database
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['logs']

    # Get the 'nginx' collection
    mongo_collection = db['nginx']

    # Get the stats
    total_logs, methods_stats, status_check_count = get_nginx_logs_stats(mongo_collection)

    # Print the stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in methods_stats.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")
