from tinydb import TinyDB
from datetime import datetime

db = TinyDB("journal_entries.json")

def save_entry(mood, text):

    db.insert({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "mood": mood,
        "text": text
    })

def get_entries():

    return db.all()