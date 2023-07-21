#!/usr/bin/env python3

# Write a Python function that changes all topics of a school document based on the name:

def insert_school(mongo_collection, **kwargs):
    # Insert the document into the collection and get the inserted _id
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id

if __name__ == "__main__":
    inserted_id = insert_school(mongo_collection, name="Example School", location="City XYZ", students=1000)
    print(f"New document inserted with _id: {inserted_id}")
