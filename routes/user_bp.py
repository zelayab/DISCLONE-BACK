from flask import Blueprint, request, render_template, session, url_for, redirect,flash
# from ..controller.userController import userController
from ..models.user import User
# from ..models.server import Server
# from ..models.channel import Channel
# from ..models.message import Message

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data['username']
        password = data['password']        
        user = User.get_user(username)
        if user:
            session['logged_in'] = True            
            session['username'] = user.username          
            return redirect('/index.html')       
        else:
            # session['logged_in'] = False
            return render_template('auth/login.html')

    return render_template('auth/login.html')

@user_bp.route('/index.html')
def index_html():
    logged_in = session.get('logged_in')
    if not logged_in:
        return redirect('/')
    print("estoy en idex")
    # # Obtener el nombre de usuario (supongo que está en session)
    user_id = session.get('user_id')
    password = session.get('password')
    username = User.get_user_by_id(user_id)

    # # Aquí debes obtener las listas server_list, channel_list, y message_list
    # server_list = Server.get_servers_from_db()
    # channel_list = Channel.get_channels_from_db()
    # message_list = Message.get_messages_from_db()

    # print(server_list[0].name)
    # print(channel_list[0])
    # print(message_list[0])
    return render_template('index.html')
# lo q falta en el render  server_list=server_list, channel_list=channel_list, message_list=message_list, logged_in=logged_in,user_id=user_id, username=username

   
    

@user_bp.route('/register', methods=['GET' ,'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        print(username, password, email)

        user = User.create_user(username, password, email)

        return redirect('/')

    return render_template('auth/register.html')


@user_bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/')

@user_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    logged_in = session.get('logged_in')
    if not logged_in:
        return redirect('/')

    user_id = session.get('user_id')
    user = User.get_user(username=None, password=None )

    if request.method == 'POST':
        data = request.form
        new_email = data['new_email']
        new_password = data['new_password']
        confirm_new_password = data['confirm_new_password']

        if new_password == confirm_new_password:
            User.update_user(user_id, new_email, new_password)
            flash("Se han actualizado los datos exitosamente", "success")
            return redirect('/profile')
        else:
            return "Las contraseñas no coinciden"
    
    return render_template('profile/profile.html', user=user, logged_in=logged_in)



#AQUI VA TODO RELACIONADO CON SERVERS

# @user_bp.route('server/create_server', methods=['GET', 'POST'])
# def create_server():
#     if request.method == 'POST':
#         data = request.form
#         name = data['name']
#         description = data['description']
#         print("estoy en server/create_server")
#         if name == "" or description == "":
#             return redirect('/index.html')
#         Server.create_server(name, description)
#         return redirect('/index.html')
#     return render_template('server/create_server.html')

# @user_bp.route('/server/delete_server/', methods=['GET', 'POST'])
# def delete_server():
#     if request.method == 'POST':
#         server_id = request.form.get('server_id')
#         Server.delete_server(server_id)
        

#     return render_template('server/delete_server.html')

# @user_bp.route('/server/<int:server_id>', methods=['GET', 'POST'])
# def server_page(server_id):
#     logged_in = session.get('logged_in')
#     if not logged_in:
#         return redirect('/')

#     server = Server.get_server_data(server_id)
#     channel_list = Channel.get_channels_from_db()
#     message_list = Message.get_messages_from_db()


#     return render_template('server/server_page.html', server=server, channel_list=channel_list, message_list=message_list, logged_in=logged_in)
#     # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
    #     email = request.form['email']
    #     print(username, password, email)

    #     user = userController.update_user(id, username, password, email)

    #     return redirect(url_for('auth/login.html'))

    # return render_template('profile/profile.html')
