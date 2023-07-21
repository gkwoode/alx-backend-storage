#!/usr/bin/env python3

# my comment

import pymongo

def get_nginx_logs_stats(mongo_collection):
    total_logs = mongo_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_stats = {method: mongo_collection.count_documents({"method": method}) for method in methods}
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    
    # Get the top 10 most present IPs in the nginx collection
    ip_pipeline = [
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        }
    ]
    
    top_ips = list(mongo_collection.aggregate(ip_pipeline))
    
    return total_logs, methods_stats, status_check_count, top_ips

if __name__ == "__main__":
    # Connect to the MongoDB server and the 'logs' database
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    
    # Get the 'nginx' collection
    mongo_collection = db['nginx']
    
    # Get the stats and top 10 IPs
    total_logs, methods_stats, status_check_count, top_ips = get_nginx_logs_stats(mongo_collection)
    
    # Print the stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in methods_stats.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")
    
    print("Top 10 IPs:")
    for idx, ip_data in enumerate(top_ips, 1):
        print(f"\t{idx}. IP: {ip_data['_id']}, Count: {ip_data['count']}")
