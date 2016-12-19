from flask import Flask
from modules.database import Database
from modules.config import get_config
from modules.steam_parser import populate_db
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

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--refresh_db":
        log.info("Refreshing steam app and language db" )
        populate_db(db)        
    else:
        application.run(host='0.0.0.0', debug=True)
