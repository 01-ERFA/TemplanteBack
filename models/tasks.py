from datetime import datetime
from utils.db import db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return '<Task %r>' %self.id

    def serialize(self):
        return{
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at
        }