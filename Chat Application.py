# app.py

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)




<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Chat Application</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.0/socket.io.js"></script>
    <style>
        #messages {
            list-style-type: none;
            margin: 0;
            padding: 0;
        }
    </style>
</head>
<body>

    <ul id="messages"></ul>
    <form id="form" action="">
        <input id="input" autocomplete="off" /><button>Send</button>
    </form>

    <script>
        var socket = io.connect('http://' + document.domain + ':' + location.port);

        socket.on('message', function(data) {
            var ul = document.getElementById('messages');
            var li = document.createElement('li');
            li.appendChild(document.createTextNode(data));
            ul.appendChild(li);
        });

        document.querySelector('form').onsubmit = function() {
            var input = document.getElementById('input');
            socket.emit('message', input.value);
            input.value = '';
            return false;
        };
    </script>

</body>
</html>
