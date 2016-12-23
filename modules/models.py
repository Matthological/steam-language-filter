from .database import db

steam_apps_langs_relationship = db.Table("steam_apps_langs", db.Model.metadata,
                                  db.Column('app_id', db.Integer, db.ForeignKey('steam_app.id')),
                                  db.Column('lang_id', db.Integer, db.ForeignKey('steam_language.id')))    

class Steam_App(db.Model):
    __tablename__ = "steam_app"
    id = db.Column(db.Integer, primary_key=True)
    steam_app_id = db.Column(db.String(10), unique=True)
    steam_app_pic = db.Column(db.LargeBinary) 
    languages = db.relationship('Steam_Languages', secondary=steam_apps_langs_relationship,
                                  backref=db.backref('apps', lazy='dynamic'))

    def __init__(self, app_id, app_pic = 0):
        self.steam_app_id = app_id
        self.steam_app_pic = app_pic
    
class Steam_Language(db.Model):
    __tablename__ = "steam_language"
    id = db.Column(db.Integer, primary_key=True)
    language_name = db.Column(db.String(100), unique=True)
    language_presentation = db.Column(db.String(15), unique=True)

    def __init__(self, name, presentation):
        self.language_name = name
        self.language_presentation = presentation
