from ..database.bd import Database


class Server:
    def __init__(self, id, name, owner_id, description):
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.description = description

    @classmethod
    def create_server(cls,name, description):
        query = "INSERT INTO servers (name,description) VALUES (%s,%s)"
        conn = Database.conectar()
        cur = conn.cursor()
        val = (name, description)
        cur.execute(query, val)
        conn.commit()
        conn.close()
        print(cur.rowcount, "Servidor creado")

    @classmethod
    def get_servers_from_db(cls):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "SELECT id, name, owner_id, description FROM servers"
        cursor.execute(query)
        resultados = cursor.fetchall()
        servidores = []
        for resultado in resultados:
            id = resultado[0]
            name = resultado[1]
            owner_id = resultado[2]
            description = resultado[3]
            servidor = Server(name, owner_id, description)
            servidor.id = id
            servidores.append(servidor)
        cursor.close()
        return servidores

    @classmethod
    def delete_server(cls,server_id):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "DELETE FROM servers WHERE id = %s"
        cursor.execute(query, (server_id,))
        conn.commit()
        cursor.close()
        return True

    @classmethod
    def get_server_data(cls,server_id):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "SELECT id, name, owner_id, description FROM servers WHERE id = %s"
        cursor.execute(query, (server_id,))
        resultado = cursor.fetchone()

        if resultado:
            id = resultado[0]
            name = resultado[1]
            owner_id = resultado[2]
            description = resultado[3]
            server = Server(name, owner_id, description)
            server.id = id
            cursor.close()
            return server
        else:
            cursor.close()
            return None
    

    @classmethod
    def update_server(cls,server_id, name, description):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "UPDATE servers SET name = %s, description = %s WHERE id = %s"
        cursor.execute(query, (name, description, server_id))
        conn.commit()
        cursor.close()
        return True
