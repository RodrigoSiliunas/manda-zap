from datetime import datetime
from app.config.database import db



class Teacher(db.Document):
    name = db.StringField(required=True)
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    subject = db.ListField()

    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)
