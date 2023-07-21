#!/usr/bin/env python3

# Write a Python function that lists all documents in a collection:

def list_all(mongo_collection):
    documents = list(mongo_collection.find({}))
    return documents

if __name__ == "__main__":
    result = list_all(mongo_collection)
    print(result)
