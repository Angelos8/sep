from pymongo import MongoClient

# Create a MongoClient instance
client = MongoClient('db', 27017)  # Replace with your container's hostname and port

# Get a reference to the "attackflow" database
db = client['attackflow']

# List of collection names to check/create
collections = ['current_documents', 'pending_documents', 'legacy_documents', 'rejected_documents', 'users']

# Check if the "attackflow" database exists
if 'attackflow' not in client.list_database_names():
    print("Creating 'attackflow' database...")
    # Create the "attackflow" database if it doesn't exist
    db = client['attackflow']
else:
    print(f'Database {db} found!')
    print(f"it contains {db.list_collection_names()}")

# Check and create collections if necessary
for collection_name in collections:
    if collection_name not in db.list_collection_names():
        print(f"Creating '{collection_name}' collection...")
        db.create_collection(collection_name)

# Close the MongoDB connection
client.close()