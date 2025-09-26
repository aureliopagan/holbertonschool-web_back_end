#!/usr/bin/env python3
"""
Returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    
    Args:
        mongo_collection: pymongo collection object
        
    Returns:
        List of students sorted by averageScore in descending order
    """
    # Use MongoDB aggregation pipeline to calculate average scores
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    
    # Execute the aggregation pipeline and return results as list
    return list(mongo_collection.aggregate(pipeline))