'''
Maqsad Chat Room v1.0.0
Author: Nikhil Kumar
GitHub: <Insert your GitHub profile URL>
Description: A chat room application designed and developed by Nikhil Kumar, a first-year student aspiring to create professional-grade projects. 
License: MIT
Year: 2024

NOTE: If you use or modify this project, please give credit to the original author.
'''

from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/<room_id>')
def room(room_id):
    return render_template('chat.html', room_id=room_id)

@socketio.on('joinRoom')
def handle_join_room(data):
    room = data.get('roomId')
    if room:
        join_room(room)
        print(f"Client joined room: {room}")

@socketio.on('sendMessage')
def handle_message(data):
    room = data.get('roomId')
    message = data.get('message')
    avatar = data.get('avatar', 'https://iili.io/20rvmEN.md.jpg')  # Default avatar

    if room and message:
        print(f"Message received in room {room}: {message}")
        # Send to all users in the room (except the sender)
        emit('receive_message', {'message': message, 'avatar': avatar}, room=room, include_self=False)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)
