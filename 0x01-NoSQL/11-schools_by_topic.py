#!/usr/bin/env python3

# Write a Python function that returns the list of school having a specific topic:

def schools_by_topic(mongo_collection, topic):
    # Find schools that have the given topic in their topics list
    schools = list(mongo_collection.find({"topics": topic}))
    return schools

if __name__ == "__main__":
    topic_to_search = "Mathematics"
    schools_with_topic = schools_by_topic(mongo_collection, topic_to_search)
    
    if schools_with_topic:
        print(f"Schools with the topic '{topic_to_search}':")
        for school in schools_with_topic:
            print(school['name'])
    else:
        print(f"No schools found with the topic '{topic_to_search}'.")
