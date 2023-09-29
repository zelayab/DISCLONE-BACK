from app.database.bd import Database


class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def create_user(cls, username, password, email):
        query = "INSERT INTO users (username,password,email) VALUES (%s,%s,%s)"
        conn = Database.conectar()
        cur = conn.cursor()
        val = (username, password, email)
        cur.execute(query, val)
        conn.commit()
        conn.close()
        print(cur.rowcount, "Usuario creado")

    @classmethod
    def get_user(cls, username, password):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "SELECT id,username,password FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        resultado = cursor.fetchone()
        print("estoy en modeluser")
        if resultado:
            id = resultado[0]
            username = resultado[1]
            password = resultado[2]
            user = User(id, username, password)
            cursor.close()
            return user
        else:
            cursor.close()
            return print("error en user bd")

    @classmethod
    def update_user(cls, user_id, email, password):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "UPDATE users SET email = %s, password = %s WHERE id = %s"
        cursor.execute(query, (email, password, user_id))
        conn.commit()
        cursor.close()
        return True

    @classmethod
    def delete_user(cls, user_id):
        conn = Database.conectar()
        cursor = conn.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        conn.commit()
        cursor.close()
        return True
