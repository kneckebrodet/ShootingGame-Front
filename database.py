from pymongo import MongoClient

class MongoDBClient:
    def __init__(self):
        self.client = None
        self.db = None
        self.collection = None

    def connect_to_localhost(self, database_name="localhost", collection_name=27017):
        self.client = MongoClient(database_name, collection_name)
        # Choose database
        self.db = self.client.ShootingGame
        # Choose collection
        self.collection = self.db.Players

    def add_new_player(self, player_data):
        self.collection.insert_one(player_data)

    def get_list_of_players(self):
        playersObject = self.collection.find({}, {"_id": 0})
        # Convert object file to list of dicts
        rankedlist = [player for player in playersObject]
        # Convert list of dicts to list of lists
        upd_list = []
        for obj in rankedlist:
            key, value = obj.popitem()
            upd_list.append([key,value])

        return upd_list