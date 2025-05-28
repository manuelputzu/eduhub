from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    lessons = db.relationship('Lesson', backref='user', lazy=True)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    lesson_title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<Lesson(id={self.id}, title='{self.lesson_title}')>"
