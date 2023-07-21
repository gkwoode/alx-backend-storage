#!/usr/bin/env python3

""" Write a Python function that returns all students sorted by average score: """

import pymongo

def top_students(mongo_collection):
    # Aggregate the data to calculate the average score for each student
    pipeline = [
        {
            "$group": {
                "_id": "$student_id",
                "averageScore": {"$avg": "$score"}
            }
        },
        {
            "$lookup": {
                "from": "students",
                "localField": "_id",
                "foreignField": "_id",
                "as": "student_data"
            }
        },
        {
            "$unwind": "$student_data"
        },
        {
            "$project": {
                "_id": "$student_data._id",
                "name": "$student_data.name",
                "averageScore": 1
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    
    top_students_list = list(mongo_collection.aggregate(pipeline))
    return top_students_list

if __name__ == "__main__":
    top_students_list = top_students(mongo_collection)

    if top_students_list:
        for student in top_students_list:
            print(f"Student ID: {student['_id']}, Name: {student['name']}, Average Score: {student['averageScore']}")
    else:
        print("No students found.")
