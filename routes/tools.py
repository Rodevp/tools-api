from controllers.tools import GetAllToolsController, GetByTagToolsController
from flask import Blueprint, jsonify, request

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



@tools.route('/tools/tag')
def get_tools_by_tag() :

    tag = request.args.get('tag')

    try: 
        controller = GetByTagToolsController()
    except ValueError as err:
        return jsonify({
            'message': f'{err}'
        })

    tools = controller.get_tools(tag)

    return jsonify(tools), 200