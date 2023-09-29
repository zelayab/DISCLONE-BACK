from ..models.server import Server

class serverController:
    @classmethod
    def get_server(cls, id):
        server = Server.get_server_data(id)
        if server is not None:
            server_response = {
                'id': server.id,
                'name': server.name,
                'description': server.description,
                'owner_id': server.owner_id
            }
            return server_response, 200
        else:
            return "Server not found", 404
    
    @classmethod
    def create_server(cls, name, description, owner_id):
        server = Server(name, description, owner_id)
        server.save()
        return server.id, 201
    
    @classmethod
    def update_server(cls, id, name, description, owner_id):
        server = Server.get_servers_from_db(id)
        if server is not None:
            server.name = name
            server.description = description
            server.owner_id = owner_id
            server.save()
            return server.id, 200
        else:
            return "Server not found", 404
