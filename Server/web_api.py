from flask import Flask
from modules.database import Database
from modules.config import get_config
from modules.steam_parser import populate_db
from flask.json import jsonify
import sys, os, logging
application = Flask(__name__)
logging.basicConfig()
log = logging.getLogger('web_api')
log.setLevel(logging.INFO)
fh = logging.FileHandler('web_api.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
log.addHandler(fh)

config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "web_api.config")
config = get_config(config_path)
log.setLevel(config['log_level'])
db = Database(application, config['db_filepath'])

@application.route('/api/language', methods=['GET'])
def get_languages():
    languages = ["English", "French", "Romanian", "Japanese", "Chinese"]
    return jsonify(languages)

@application.route('/api/filter/game', methods=['POST'])
def apply_game_filter():
    return

# This is temporarily added to allow running index.html from file
@application.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'null')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == "__main__":
    # TODO: elaborate on this (a --debug flag + a --host flag)
    application.run(host='0.0.0.0', debug=True)
