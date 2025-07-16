# sample_data.py

from models import Category, Hadith, Dua, PrayerTime
from datetime import datetime

def insert_sample_data(db):
    # Check if data already exists
    if Category.query.first() is None:
        # Create categories
        categories = [
            Category(name="Hadith", description="Prophetic traditions"),
            Category(name="Dua", description="Islamic supplications"),
            Category(name="Quran", description="Holy Quran verses"),
            Category(name="Prayer", description="Daily prayers and rituals"),
            Category(name="Akhlaq", description="Islamic character and morals"),
            Category(name="Fiqh", description="Islamic jurisprudence")
        ]
        
        for cat in categories:
            db.session.add(cat)
        db.session.commit()
        
        # Add sample hadiths
        hadith_category = Category.query.filter_by(name="Hadith").first()
        prayer_category = Category.query.filter_by(name="Prayer").first()
        
        sample_hadiths = [
            Hadith(
                narrator="Abu Hurairah",
                arabic="إنما الأعمال بالنيات وإنما لكل امرئ ما نوى",
                english="Actions are according to intentions, and everyone will get what was intended",
                transliteration="Innama al-a'malu bin-niyyat wa innama li-kulli imri'in ma nawa",
                source="Sahih Bukhari",
                book="Book of Revelation",
                hadith_number=1,
                grade="Sahih",
                category=hadith_category
            ),
            Hadith(
                narrator="Abdullah ibn Amr",
                arabic="المسلم من سلم المسلمون من لسانه ويده",
                english="The Muslim is the one from whose tongue and hand the Muslims are safe",
                transliteration="Al-Muslimu man salima al-Muslimuna min lisanihi wa yadihi",
                source="Sahih Bukhari",
                book="Book of Faith",
                hadith_number=10,
                grade="Sahih",
                category=hadith_category
            ),
            Hadith(
                narrator="Abu Hurairah",
                arabic="من صلى علي واحدة صلى الله عليه عشرا",
                english="Whoever sends blessings upon me once, Allah will send blessings upon him ten times",
                transliteration="Man salla alayya wahidatan salla Allahu alayhi ashran",
                source="Sahih Muslim",
                book="Book of Prayer",
                hadith_number=408,
                grade="Sahih",
                category=prayer_category
            )
        ]
        
        for hadith in sample_hadiths:
            db.session.add(hadith)
        
        # Add sample duas
        dua_category = Category.query.filter_by(name="Dua").first()
        
        sample_duas = [
            Dua(
                title="Morning Dua",
                arabic="أصبحنا وأصبح الملك لله، والحمد لله",
                transliteration="Asbahna wa asbahal-mulku lillah, walhamdu lillah",
                english="We have reached the morning and with it the sovereignty belongs to Allah, and praise is to Allah",
                occasion="Morning",
                source="Sahih Muslim",
                category=dua_category
            ),
            Dua(
                title="Before Eating",
                arabic="بسم الله",
                transliteration="Bismillah",
                english="In the name of Allah",
                occasion="Before eating",
                source="Sahih Bukhari",
                category=dua_category
            )
        ]
        
        for dua in sample_duas:
            db.session.add(dua)
        
        # Add sample prayer times
        today = datetime.now().date()
        prayer_time = PrayerTime(
            location="Default Location",
            date=today,
            fajr="05:30",
            dhuhr="12:15",
            asr="15:45",
            maghrib="18:20",
            isha="19:45"
        )
        db.session.add(prayer_time)
        
        db.session.commit()