import os, sys, logging
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from models import * #getting around cyclic imports

log = logging.getLogger('{0}.{1}'.format("web_api", "database"))


class Database(object):
    def __init__(self, flask_app, db_path):
        self.db_filepath = db_path
        self.flask_app = flask_app 
        self.flask_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{0}".format(db_path)
        self.flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        db.init_app(flask_app) 
        self.create_db_if_absent()

    
    def create_db_if_absent(self):
        if not os.path.isfile(self.db_filepath):
            log.info("Couldn't find db file at '{0}'. Creating it there now.".format(self.db_filepath))
            with self.flask_app.app_context():
                db.create_all()
        else:
            log.debug("Found db file at '{0}'.")


if __name__ == "__main__":
    from flask import Flask
     
    a = Database(Flask("somename"), "/web/db.sqlite")
