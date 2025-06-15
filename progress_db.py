import sqlite3
from datetime import datetime

DB_NAME = "user_progress.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            concept TEXT,
            question TEXT,
            correct INTEGER,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_answer(concept, question, correct):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO progress (concept, question, correct, timestamp)
                 VALUES (?, ?, ?, ?)''',
              (concept, question, int(correct), datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_concept_accuracy(concept):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''SELECT COUNT(*), SUM(correct) FROM progress WHERE concept = ?''', (concept,))
    total, correct = c.fetchone()
    conn.close()
    if total == 0:
        return 1.0  
    return correct / total

def show_progress_summary():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT concept,
               COUNT(*) as total,
               SUM(correct) as correct,
               ROUND(100.0 * SUM(correct) / COUNT(*), 1) as accuracy
        FROM progress
        GROUP BY concept
        ORDER BY accuracy ASC
    ''')
    rows = c.fetchall()
    conn.close()

    print("\n📊 Progress Summary:")
    for concept, total, correct, accuracy in rows:
        print(f"- {concept}: {correct}/{total} correct ({accuracy}%)")

