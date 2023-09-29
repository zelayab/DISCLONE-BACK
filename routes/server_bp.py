from flask import Blueprint, request, render_template, session,redirect
from ..models.server import Server
from ..models.channel import Channel
from ..models.message import Message
from ..models.user import User


server_bp = Blueprint('server_bp', __name__)

@server_bp.route('server/create_server', methods=['GET', 'POST'])
def create_server():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        description = data['description']
        print("estoy en server/create_server")
        if name == "" or description == "":
            return redirect('/index.html')
        Server.create_server(name, description)
        return redirect('/index.html')
    return render_template('server/create_server.html')

@server_bp.route('/server/delete_server/', methods=['GET', 'POST'])
def delete_server():
    if request.method == 'POST':
        server_id = request.form.get('server_id')
        Server.delete_server(server_id)
        

    return render_template('server/delete_server.html')

@server_bp.route('/server/<int:server_id>', methods=['GET', 'POST'])
def server_page(server_id):
    logged_in = session.get('logged_in')
    if not logged_in:
        return redirect('/')

    server = Server.get_server_data(server_id)
    channel_list = Channel.get_channels_from_db()
    message_list = Message.get_messages_from_db()


    return render_template('server/server_page.html', server=server, channel_list=channel_list, message_list=message_list, logged_in=logged_in)