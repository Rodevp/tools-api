from DTO.tools import ToolDTO
from repositories.tools import ToolsRepository

class GetAllToolsServices :
    
    def __init__(self) :
        pass


    def get(self) :
        
        try: 
            repository = ToolsRepository()
        except Exception as err :
            raise ValueError('error al obtener tags')

        list_tools = []

        for item in repository.get_all() :

            tool_dto = ToolDTO (
                item['_id']['$oid'], item['title'], item['link'], item['description'], item['tags']
            )
            
            tool = {
                'id': tool_dto.id,
                'title': tool_dto.title,
                'link': tool_dto.link,
                'description': tool_dto.description,
                'tags': tool_dto.tags
            }

            list_tools.append(tool)

        return list_tools


class GetByTagToolsService :

    def __init__(self) :
        pass


    def get(self, tag) :
        
        try :
            get_all_service = GetAllToolsServices()
        except Exception as err :
            raise ValueError('Error de servicio')
        

        def filter_tool(tool) :

            if  tag in tool['tags']:
                return True
            
            return False

        filter_tools_by_task = list( filter ( filter_tool, get_all_service.get() ) )

        print(filter_tools_by_task)

        return filter_tools_by_task


class SaveToolService :

    def __init__(self) :
        pass


    def save(self, tool) :
        
        try :
            repository = ToolsRepository()
        except Exception as err :
            raise ValueError('error de servicio')

        tool_response = repository.save(tool)

        tool_dto = ToolDTO(
            tool_response['_id'], tool_response['title'], tool_response['link'], 
            tool_response['description'], tool_response['tags']
        )

        tool_parse = {
            'title': tool_dto.title,
            'link': tool_dto.link,
            'description': tool_dto.description,
            'tags': tool_dto.tags
        }

        if not tool_response == None :
            return tool_parse

        