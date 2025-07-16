from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    hadiths = db.relationship('Hadith', backref='category', lazy=True)
    duas = db.relationship('Dua', backref='category', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Hadith(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    narrator = db.Column(db.String(100), nullable=False)
    arabic = db.Column(db.Text, nullable=False)
    english = db.Column(db.Text, nullable=False)
    transliteration = db.Column(db.Text)
    source = db.Column(db.String(100), nullable=False)
    book = db.Column(db.String(100))
    hadith_number = db.Column(db.Integer)
    grade = db.Column(db.String(20))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'narrator': self.narrator,
            'arabic': self.arabic,
            'english': self.english,
            'transliteration': self.transliteration,
            'source': self.source,
            'book': self.book,
            'hadith_number': self.hadith_number,
            'grade': self.grade,
            'category': self.category.to_dict() if self.category else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Dua(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    arabic = db.Column(db.Text, nullable=False)
    transliteration = db.Column(db.Text)
    english = db.Column(db.Text, nullable=False)
    occasion = db.Column(db.String(100))
    source = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'arabic': self.arabic,
            'transliteration': self.transliteration,
            'english': self.english,
            'occasion': self.occasion,
            'source': self.source,
            'category': self.category.to_dict() if self.category else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class PrayerTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    fajr = db.Column(db.String(10), nullable=False)
    dhuhr = db.Column(db.String(10), nullable=False)
    asr = db.Column(db.String(10), nullable=False)
    maghrib = db.Column(db.String(10), nullable=False)
    isha = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'location': self.location,
            'date': self.date.isoformat() if self.date else None,
            'prayer_times': {
                'fajr': self.fajr,
                'dhuhr': self.dhuhr,
                'asr': self.asr,
                'maghrib': self.maghrib,
                'isha': self.isha
            },
            'created_at': self.created_at.isoformat() if self.created_at else None
        }