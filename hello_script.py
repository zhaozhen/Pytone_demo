from flask_script import Manager
from flask import Flask
app = Flask(__name__)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()