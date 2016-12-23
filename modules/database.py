import os, sys, logging
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from .models import * #getting around cyclic imports

log = logging.getLogger('{0}.{1}'.format("web_api", "database"))


class Database(object):
    def __init__(self, flask_app, db_path):
        self.db_filepath = db_path
        self.flask_app = flask_app 
        self.flask_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{0}".format(db_path)
        self.flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            
        db.init_app(flask_app) 
        self.create_db_if_absent()

        self.all_appids = None
        self.all_languages = None

    
    def create_db_if_absent(self):
        
        if not os.path.isfile(self.db_filepath):
            log.info("Couldn't find db file at '{0}'. Creating it there now.".format(self.db_filepath))
            with self.flask_app.app_context():
                 db.create_all()
        else:
            log.debug("Found db file at '{0}'.".format(self.db_filepath))


    def get_app(self, app_id):
        pass

    def add_app_language(self, app_id, app_name, app_pic_src, languages):
        app = self.get_app(app_id)
        if not app:
            log.debug("App {} ({}) doesn't exist in DB, adding it".format(app_name, app_id))
            app = self.add_app(app_id, app_name, app_pic_src)

        for name, media in languages:
            lang = self.get_lang(name, media)
            if not lang:
                log.debug("Lang {} -  {} doesn't exist in DB, adding it".format(name, media))
                lang = self.add_language_entry(name, media)

            app_lang_junction = self.get_app_lang_junction(app, lang)
            if not app_lang_junction:
                log.debug("Relationship between app {} ({}) and Lang {} -  {} doesn't exist in DB, adding it".format(app_name, app_id, name, media))
                self.add_app_lang_junction(app, lang)

    def add_app(self, app_id, app_name, app_pic_src):
        pass

    def get_lang(self, name, media):
        pass

    def add_language_entry(self, name, media):
        pass

    def get_app_lang_junction(self, app, lang):
        pass

    def add_app_lang_junction(self, app, lang):
        pass

