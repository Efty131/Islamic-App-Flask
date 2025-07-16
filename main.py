from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
import os
from models import db, Hadith  # Import Hadith model
from sample_data import insert_sample_data

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "islamic_app.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
    insert_sample_data(db)

@app.route('/')
def home():
    return "Welcome to the Islamic Flask App!"

@app.route('/api/hadiths')
def get_hadiths():
    hadiths = Hadith.query.all()
    result = []
    for hadith in hadiths:
        result.append({
            "id": hadith.id,
            "narrator": hadith.narrator,
            "arabic": hadith.arabic,
            "english": hadith.english,
            "transliteration": hadith.transliteration,
            "source": hadith.source,
            "book": hadith.book,
            "hadith_number": hadith.hadith_number,
            "grade": hadith.grade,
            "category": hadith.category.name if hadith.category else None
        })
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)