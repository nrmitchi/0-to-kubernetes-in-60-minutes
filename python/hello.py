from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! I am version "{}" running on host "{}"'.format(
        os.getenv('VERSION', 'Unknown'),
        socket.gethostname()
    )
