from flask import Flask, jsonify
from services.tools import GetAllToolsServices

app = Flask(__name__)


@app.route('/')
def index() :
    service = GetAllToolsServices()
    list_tools = service.get()
    return jsonify( list_tools )



if __name__ == '__main__' :
    app.run(debug=True, port=3001)