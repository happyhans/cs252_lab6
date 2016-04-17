from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')
    
@socketio.on('connect')
def connect():
    print 'connection'
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def disconnect():    
    print 'disconnect'
    
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port=8080)