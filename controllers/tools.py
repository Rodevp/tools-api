from services.tools import GetAllToolsServices, GetByTagToolsService

class GetAllToolsController :

    def __init__(self) :
        pass


    def get(self) :

        try:
            service = GetAllToolsServices()
        except ValueError as err :
            raise ValueError(err)

        if len( service.get() ) == 0 :
            return []

        return service.get()


class GetByTagToolsController :

    def __init__(self) :
        pass


    def get_tools(self, tag) :
        
        try :
            service = GetByTagToolsService()
        except ValueError as err :
            raise ValueError(err)
        

        tools = service.get(tag)

        return tools