from db import init_db
from bson import json_util, ObjectId
import json

class ToolsRepository :

    _client = init_db()
    _db = _client['tools']

    def __init__(self) :
        pass


    def get_all(self) :

        tools_collection = json.loads(  json_util.dumps( self._db['tools'].find()   )   )
        return tools_collection

