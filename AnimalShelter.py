from pymongo import MongoClient

from bson.objectid import ObjectId





class AnimalShelter(object):

    """ CRUD operations for Animal collection in MongoDB """



    def __init__(self, database_name, port_number, username, password, collection_name):

        self.username = username

        self.password = password

        # Initializing the MongoClient. This helps to

        # access the MongoDB databases and collections.

        self.client = MongoClient(

            "mongodb://{0}:{1}@localhost:{2}/{3}".format(username, password, port_number, database_name))

        self.database = self.client[database_name]

        self.collection = self.database[collection_name]



    # Complete this create method to implement the C in CRUD.

    def create(self, data):

        if data is not None:

            result = self.collection.insert(

                data)  # data should be dictionary

            if result != 0:

                return True

            else:

                return False

        else:

            raise Exception("Nothing to save, because data parameter is empty")



    # Create method to implement the R in CRUD.

    def read(self, criteria):

        # make sure criteria isn't None

        if criteria:

            # search for data

            data = self.collection.find(criteria, {"_id": 0})

        else:

            data = self.collection.find({}, {"_id": 0})

            # raise Exception(

            #     "Nothing to read, because criteria parameter is empty")



        # return found data

        return data



    # update an object from the database

    def update(self, criteria, update):

        # make sure criteria isn't None

        if criteria:

            data = self.collection.update_one(criteria, {"$push": update}, upsert=False, multi=False)

        else:

            raise Exception(

                "Nothing to read, because criteria parameter is empty")



        # return found data  

        return data





    # delete an object from the database

    def delete(self, criteria):

        # make sure criteria isn't None

        if criteria:

            data = self.collection.delete_one(criteria)

        else:

            raise Exception(

                "Nothing to read, because criteria parameter is empty")



        # return found data  

        return data

