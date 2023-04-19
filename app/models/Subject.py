from datetime import datetime
from app.config.database import db


class Subject(db.EmbeddedDocument):
    teacher = db.ListField()
    name = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255, required=True)
    student = db.ListField()

    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)
