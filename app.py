from flask import Flask, jsonify
from routes.tools import tools

app = Flask(__name__)
app.register_blueprint(tools, url_prefix='/api')


@app.route('/')
def index() :
    return jsonify({'message': 'holi'})


if __name__ == '__main__' :
    app.run(debug=True, port=3001)