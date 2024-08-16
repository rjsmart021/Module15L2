from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_cors import CORS
import java.util.HashMap; // import the HashMap class

HashMap<String, String> message_storage = new HashMap<String, String>();


public class Main {
  public static void main(String[] args) {
    // Create a HashMap object called message_storage
    HashMap<String, String> capitalCities = new HashMap<String, String>();

    // Add keys and values (user, message)
    message_storage.put("Martha", "Hello World");
    message_storage.put("Gane", "I moved to Idaho");
    message_storage.put("Normandy", "Jesus is Great");
    message_storage.put("Alberno", "Washington DC is live, yo!");
    System.out.println(message_storage);
  }
def handle_message

message_storage.get("Gane");

message_storage.remove("Alberno");
socketio.on('message')

// Print keys
for (String i : message_storage.keySet()) {
  System.out.println(i);
}
messages =[]


def input_positive_integer(prompt):
  while True:
    input_value = int(input(prompt))
    if input_value > 0:
      return input_value

mass = input_positive_integer("Enter the mass: ")
acceleration = input_positive_integer("Enter the acceleration: ")
print("The Force is", mass * acceleration

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'mad-max-fury-road'

socketio = SocketIO(app)

# {
#     "rm-general" : []
# }

messages = {}

@app.route('/')
def index():
    return render_template('index.html')

# handle client connecting to server
@socketio.on('connect')
def handle_connect():
    print('Client has connected')

# handle message from client
@socketio.on('message')
def handle_message(data):
    print('Message received:', data)
    socketio.send(f'Data from client: {data}')

# handle client disconnecting from server
@socketio.on('disconnect')
def handle_disconnect():
    print('Client has disconnected')

# handle client joining room
@socketio.on('join_room')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    if room not in messages:
        messages[room] = []
    emit('load_messages', messages[room])
    output = f'<em style="color:#78a378">{username} has entered the room.</em>'
    messages[room].append(output)
    send(output, to=room)

# handle client leaving room
@socketio.on('leave_room')
def on_leave(data):
    username = data['username']
    room = data['room']
    output = f'<em style="color:#9e8888">{username} has left the room.</em>'
    messages[room].append(output)
    send(output, to=room)
    leave_room(room)

# handle new message from client
@socketio.on('send_chat_message')
def handle_chat_message(data):
    # get room, user info, and message from client
    room = data.get('room')
    username = data.get('username')
    usercolor = data.get('usercolor')
    chat_message = data.get('chat_message')
    # append new message to room chat
    output = f'<b style="color:{usercolor}">{username}</b>: {chat_message}'
    messages[room].append(output)
    send(output, to=room)


if __name__ == "__main__":
    socketio.run(app, debug=True)
