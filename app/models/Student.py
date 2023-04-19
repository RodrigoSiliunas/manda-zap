from datetime import datetime
from app.config.database import db


class Student(db.Document):
    identification = db.IntField()
    name = db.StringField(required=True)
    username = db.StringField(required=True)
    email = db.EmailField(required=True)
    password = db.StringField(required=True)
    subject = db.ListField()

    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)
