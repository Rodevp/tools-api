from services.tools import GetAllToolsServices


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