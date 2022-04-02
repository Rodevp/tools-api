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