from flask import request
from ..models.user import User


class userController:
    # a probar, este metodo deberia devolver un objeto de tipo user
    @classmethod
    def get_user(cls, username,password):
        user = User.get_user(username, password)
        if user is not None:
            user_response = {
                'id': user.id,
                'username': user.username,
                #'password': user.password,
                # 'email': user.email
            }
            return user_response, 200
        else:
            return {'message': 'User not found'}, 404

    

    @classmethod
    def create_user(cls, username, password, email):
        user = User.create_user(username, password, email)
        return user
       

    @classmethod
    def update_user(cls,password,email):#quiero traer al objeto user por su id y luego editar solo mail y password        
        
        user = User.get_user(password,email)
        if user is not None:
            user.password = password
            user.email = email
            return user
        else:
            return {'message': 'User not found'}, 404
        

    @classmethod
    def delete_user(cls, user_id):
        user_id = User.delete_user('user_id')
        return print(user_id)
    

    # @classmethod
    # def get_users():
    #     query = "SELECT * FROM users"
    #     params = None
    #     result = Database.fetch_all(query,params)
    #     Database.closeConn()
    #     if (result is not None):
    #         return User.get_user(result)
