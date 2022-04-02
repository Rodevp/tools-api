from controllers.tools import GetAllToolsController
from flask import Blueprint, jsonify

tools = Blueprint('tools', __name__)

@tools.route('/tools', methods=['GET'])
def get_all_tools() :

    try :
        controller = GetAllToolsController()
    except ValueError as err :

        return jsonify({
            'message': f'{err}'
        }), 400


    return jsonify( controller.get() ), 200
