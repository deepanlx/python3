from pymongo import MongoClient

class MongoInit(object):

    def __init__(self, collection_name, method, query=""):
        self.mongo_client = ""
        self.database_name = "ppp"
        self.collection_name = collection_name
        self.method = method
        self.query = query
        self.database = ""
        self.collection_data = ""

    def __enter__(self):
        try:
            self.db_client = MongoClient('localhost:27017')
            self.database = self.db_client[self.database_name]
            self.collection_data = self.database[self.collection_name]
            response = exec('self.' + self.method + '()')
        except Exception as error:
            print(error)

    def insert(self):
        for record in self.query:
           response = self.collection_data.insert(record)
           print(response)

    def find(self):
        response = self.collection_data.find({"sample": "test"})
        for content in response:
            print(content)

    def __exit__(self, exe_type, exc_val, exc_tb):
        if self.mongo_client:
            self.mongo_client.close()

class PPPMongoOperations(MongoInit):

    def __init__(self, collection_name, method, query=""):
        super().__init__(collection_name, method, query)

    def __enter__(self):
        super().__enter__()

if __name__ == "__main__":
    with PPPMongoOperations("deepan", 'find', {"sample": "test"}) as mongo:
        pass
