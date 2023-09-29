from database.bd import Database


class Message:
    def __init__(self, id,content , user_id, channel_id):
        self.id = id
        self.content = content
        self.user_id = user_id
        self.channel_id = channel_id
    @classmethod
    def create_message(cls,content,user_id,channel_id,author):
        query = "INSERT INTO messages (content,user_id,channel_id) VALUES (%s,%s,%s,%s)"
        conn = Database.conectar()
        cur = conn.cursor()
        val = (content,user_id,channel_id,author)
        cur.execute(query,val)
        conn.commit()
        conn.close()
        print(cur.rowcount, "Mensaje creado")
    @classmethod
    def get_messages_from_db(cls):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "SELECT * FROM messages"
        cursor.execute(query)
        resultados = cursor.fetchall()
        mensajes = []
        for resultado in resultados:
            id = resultado[0]
            content = resultado[1]
            user_id = resultado[2]
            channel_id = resultado[3]
            author = resultado[4]
            mensaje = Message(content, user_id, channel_id,author)
            mensaje.id = id
            mensajes.append(mensaje)
        cursor.close()
        return mensajes
    @classmethod
    def update_message(cls,message_id, content):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "UPDATE messages SET content = %s WHERE id = %s"
        cursor.execute(query, (content, message_id))
        conn.commit()
        cursor.close()
        return True
    @classmethod
    def delete_message(cls,message_id):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "DELETE FROM messages WHERE id = %s"
        cursor.execute(query, (message_id,))
        conn.commit()
        cursor.close()
        return True
    @classmethod
    def send_message(cls,content, user_id, channel_id):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "INSERT INTO messages (content, user_id, channel_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (content, user_id, channel_id))
        conn.commit()
        cursor.close()
        return True
    @classmethod
    def get_messages_for_channel(cls,channel_id):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "SELECT id, content, user_id, channel_id,author,created_at FROM messages WHERE channel_id = %s"
        cursor.execute(query, (channel_id,))
        resultados = cursor.fetchall()
        messages = []
        for resultado in resultados:
            id = resultado[0]
            content = resultado[1]
            user_id = resultado[2]
            channel_id = resultado[3]
            author= resultado[4]
            created_at = resultado[5]
            message = Message(content, user_id, channel_id,author,created_at)
            message.id = id
            messages.append(message)
        cursor.close()
        return messages