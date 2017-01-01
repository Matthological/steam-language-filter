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


config_filename = "web_api.config"
config_path = "{0}/{1}".format(os.path.dirname(os.path.realpath(__file__)), config_filename)

default_db_filename = "web_api.sql"
db_path = "{0}/{1}".format(os.path.dirname(os.path.realpath(__file__)), default_db_filename)

default_log_level = "DEBUG"


config = get_config(config_path, db_path, default_log_level)

log.setLevel(config['log_level'])
db = Database(application, config['db_filepath'])

@application.route('/api/language')
def get_all_languages():
    languages = ["English", "French", "Romanian", "Japanese", "Chinese"]
    return jsonify(languages)

# This is temporarily added to allow running index.html from file
@application.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'null') 
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--refresh_db":
        log.info("Refreshing steam app and language db" )
        populate_db(db)        
    else:
        application.run(host='0.0.0.0', debug=True)
