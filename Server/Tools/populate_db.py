import sys, os, logging
# Doing this because we need access to a sibling module yet we can't directly refer to the parent since its name contains hypens
sys.path.append(os.path.realpath(os.chdir("..")))
from flask import Flask
from modules.database import Database
from modules.config import get_config
from modules.steam_parser import populate_db
application = Flask(__name__)

logging.basicConfig()
log = logging.getLogger('populate_db')
log.setLevel(logging.INFO)
fh = logging.FileHandler('populate_db.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
log.addHandler(fh)

config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "web_api.config")
config = get_config(config_path)

log.setLevel(config['log_level'])
print(__name__)
db = Database(application, config['db_filepath']) # TODO: can we get rid of the dependency to application / Flask?

if __name__ == "__main__":
    log.info("Refreshing steam app and language db")
    populate_db(db)   

# Script features: 
# - Refresh languages
# - Refresh games
# - Dump all data
# - Append new data
# - Store failed pages for analysis
# - Non-saved parse
# - Parse only IDs from file

# Modifiers:
# - Number of games to parse
# - Number of new entries to fetch
# - Number of failed webpages to store
# - Whether we should store failed webpages in refreshable area or not

