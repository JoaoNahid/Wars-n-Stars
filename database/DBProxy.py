import sqlite3


class DBProxy:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.connection.execute('''
            CREATE TABLE IF NOT EXISTS highscore(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score BIGINT DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

    def update_or_create_score(self, new_score):
        score = self.connection.execute('SELECT id FROM highscore LIMIT 1')
        score = score.fetchone()

        if score:
            query = '''
                    UPDATE highscore 
                    SET score = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                '''
            self.connection.execute(query, (new_score, score[0]))
        else:
            query = '''
                    INSERT INTO highscore (score, created_at, updated_at)
                    VALUES (?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                '''
            self.connection.execute(query, (new_score,))
        self.connection.commit()

    def get_score(self):
        try:
            query = self.connection.execute('SELECT score FROM highscore LIMIT 1')
            result = query.fetchone()
            return result[0] if result else 0
        except Exception as e:
            print(f"Failed to fetch score: {e}")
            return 0
