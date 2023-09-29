from database.bd import Database


class Channel:
    def __init__(self, id, name, server_id, type=None):
        self.id = id
        self.name = name
        self.server_id = server_id
        self.type = type

    @classmethod
    def create_channel(cls, name, server_id):
        query = "INSERT INTO channels (name,server_id) VALUES (%s,%s)"
        conn = Database.conectar()
        cur = conn.cursor()
        val = (name, server_id)
        cur.execute(query, val)
        conn.commit()
        conn.close()
        print(cur.rowcount, "Canal creado")

    @classmethod
    def get_channels_from_db(cls):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "SELECT id, name, server_id FROM channels"
        cursor.execute(query)
        resultados = cursor.fetchall()
        canales = []
        for resultado in resultados:
            id = resultado[0]
            name = resultado[1]
            server_id = resultado[2]
            canal = Channel(name, server_id)
            canal.id = id
            canales.append(canal)
        cursor.close()
        return canales

    @classmethod
    def get_channels_from_server_id(cls,server_id):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "SELECT id, name, server_id FROM channels WHERE server_id = %s"
        cursor.execute(query, (server_id,))
        resultados = cursor.fetchall()
        channels = []
        for resultado in resultados:
            id = resultado[0]
            name = resultado[1]
            server_id = resultado[2]
            channel = Channel(name, server_id, type)
            channel.id = id
            channels.append(channel)
        cursor.close()
        return channels

    @classmethod
    def delete_channel(cls,channel_id):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "DELETE FROM channels WHERE id = %s"
        cursor.execute(query, (channel_id,))
        conn.commit()
        cursor.close()
        return True
    # metodo agregado para actualizar el nombre del canal
    @classmethod
    def update_channel(cls,channel_id, name):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "UPDATE channels SET name = %s WHERE id = %s"
        cursor.execute(query, (name, channel_id))
        conn.commit()
        cursor.close()
        return True
