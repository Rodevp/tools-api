from pymongo import MongoClient

def init_db() :
    try :
        client = MongoClient('mongodb://localhost:27017/')
        return client
    except Exception as err: 
        raise ValueError('aaaaaaaaaa')