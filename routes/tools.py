from controllers.tools import DeleteToolController, GetAllToolsController, GetByTagToolsController, SaveToolController
from flask import Blueprint, jsonify, request

tools = Blueprint('tools', __name__)

@tools.route('/tools', methods=['GET', 'POST'])
def get_all_tools() :

    if request.method == 'GET' :
        
        try :
            controller = GetAllToolsController()
        except ValueError as err :
            
            return jsonify({
                 'message': f'{err}'
            }), 400
            
        return jsonify( controller.get() ), 200

     
    if request.method == 'POST' :

        tool_data = request.get_json(force=True) 
        
        try :
            controller = SaveToolController()
        except ValueError as err :
            return jsonify({
                'message': f'{err}'
            }), 400

        tool = controller.save(tool_data)

        return jsonify(tool), 201


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



@tools.route('/tools/<id>', methods=['DELETE'])
def delete_tool(id) :

    try :
        controller = DeleteToolController()
    except ValueError as err :
        return jsonify({
            'message': f'{err}'
        })

    response = controller.delete(id)

    return jsonify({'message': 'destroy!'})