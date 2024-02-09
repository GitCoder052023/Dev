import pymongo


class DB_manager:
    def __init__(self, connection_string, database="Dev's Database", collection="Dev's collection"):
        # Replace with your MongoDB connection string
        self.connection_string = connection_string
        self.database = database
        self.collection = collection

        # Create a MongoClient
        self.client = pymongo.MongoClient(connection_string)
        pass

    def connect(self):
        # Replace with your MongoDB connection string
        connection_string = self.connection_string

        # Create a MongoClient
        client = pymongo.MongoClient(connection_string)

        # Access a specific database
        db = client[self.database]
        return db

    def create(self, data):
        """Insert a single document into the collection."""
        try:
            result = self.client[self.database][self.collection].insert_one(data)
            return result
        except Exception as e:
            return e

    def read(self, query=None):
        """Find documents in the collection, optionally filtering by a query."""
        try:
            if query:
                result = self.client[self.database][self.collection].find(query)
            else:
                result = self.client[self.database][self.collection].find()
            return list(result)
        except Exception as e:
            return e

    def update(self, query, update_data):
        """Update matching documents in the collection."""
        try:
            result = self.client[self.database][self.collection].update_many(query, {"$set": update_data})
            return result.modified_count
        except Exception as e:
            return e

    def delete(self, query):
        """Delete matching documents from the collection."""
        try:
            result = self.client[self.database][self.collection].delete_many(query)
            return result.deleted_count
        except Exception as e:
            return e

    def create_bulk(self, documents):
        """Insert multiple documents into the collection."""
        try:
            result = self.client[self.database][self.collection].insert_many(documents)
            return len(result.inserted_ids)
        except Exception as e:
            print("Error creating documents:", e)
            return 0

    def update_bulk(self, query, update_data):
        """Update multiple documents in the collection."""
        try:
            result = self.client[self.database][self.collection].update_many(query, {"$set": update_data})
            return result.modified_count
        except Exception as e:
            print("Error updating documents:", e)
            return 0

    def delete_bulk(self, query):
        """Delete multiple documents from the collection."""
        try:
            result = self.client[self.database][self.collection].delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("Error deleting documents:", e)
            return 0

    def create_database(self, database_name, collection_name):
        db = self.client[database_name]
        collection = db[collection_name]
        return collection

    def create_collection(self, collection_name):
        """Create a new collection in the database."""
        try:
            db = self.client[self.database]
            collection = db.create_collection(collection_name)
            return collection
        except Exception as e:
            print("Error creating collection:", e)
            return None

    def delete_collection(self, collection_name):
        """Create a new collection in the database."""
        try:
            db = self.client[self.database]
            collection = db.drop_collection(collection_name)
            return collection
        except Exception as e:
            print("Error deleting collection:", e)
            return None




