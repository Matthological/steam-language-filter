from flask import Flask
from modules.database import Database
application = Flask(__name__)

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
