from pymongo import MongoClient


class DevAuth:
    def __init__(self, db_uri, db_name='mydb', collection_name='users'):
        """
        Initialize the MongoDB authentication class.

        Args:
            db_uri (str): MongoDB connection URI.
            db_name (str, optional): Database name. Defaults to 'mydb'.
            collection_name (str, optional): Collection name for user data. Defaults to 'users'.
        """
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def register_user(self, username, password: str | int):
        """
        Register a new user.

        Args:
            username (str): User's username.
            password (str): User's password.
        """
        user_data = {'username': username, 'password': password}
        self.collection.insert_one(user_data)

    def delete_user(self, username):
        """
        Delete a user.

        Args:
            username (str): User's username.
        """
        self.collection.delete_one({'username': username})

    def update_user(self, username, new_password):
        """
        Update a user's password.

        Args:
            username (str): User's username.
            new_password (str): New password.
        """
        self.collection.update_one({'username': username}, {'$set': {'password': new_password}})

    def authenticate_user(self, username, password):
        """
        Authenticate a user.

        Args:
            username (str): User's username.
            password (str): User's password.

        Returns:
            bool: True if authentication succeeds, False otherwise.
        """
        user = self.collection.find_one({'username': username, 'password': password})
        return user is not None

    def fetch_user_details(self, username):
        """
        Fetch user details.

        Args:
            username (str): User's username.

        Returns:
            dict: User details (including roles, etc.) or None if user not found.
        """
        user = self.collection.find_one({'username': username})
        return user
