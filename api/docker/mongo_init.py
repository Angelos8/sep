# init-mongo.py
from pymongo import MongoClient

print('hffhdfkghkjdf')

# # Connect to MongoDB
# client = MongoClient('mongodb://root:example@db:27017/')

# # Create or access the database
# db = client['mydatabase']

# # Create collections
# users_collection = db['users']
# current_docs_collection = db['current_docs']
# pending_docs_collection = db['pending_docs']
# legacy_docs_collection = db['legacy_docs']
# rejected_docs_collection = db['rejected_docs']

# # Optionally, insert some initial data into collections
# users_collection.insert_many([
#     {"username": "user1", "email": "user1@example.com"},
#     {"username": "user2", "email": "user2@example.com"},
# ])

# # You can insert data into other collections similarly if needed
# # Create a user
# print(users_collection.find({}))