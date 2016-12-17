from flask import Flask
from modules.database import Database
from modules.config import get_config
import sys, os, logging
application = Flask(__name__)

logging.basicConfig()
log = logging.getLogger('web_api')
log.setLevel(logging.INFO)

config_filename = "web_api.config"
config_path = "{0}/{1}".format(os.path.dirname(os.path.realpath(__file__)), config_filename)
config = get_config(config_path)

log.setLevel(config['log_level'])
db = Database(config['db_file'])




if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--refresh_db":
        print "Refreshing" 
    else:
        application.run(host='0.0.0.0', debug=True)
