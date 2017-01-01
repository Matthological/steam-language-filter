from web_api import db
from modules.steam_parser import populate_db
import logging
log = logging.getLogger('{0}.{1}'.format("web_api", "database"))
log.info("Refreshing db with data from the Steam catalogue")
populate_db(db)