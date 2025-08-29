from datetime import datetime

from database.Models import HighScore
from peewee import DoesNotExist
from typing import List, Optional

class HighScoreService:

    @staticmethod
    def create_or_update_score(score):
        try:
            existing_record = HighScore.select().first()
            if existing_record:
                if score > existing_record.score:
                    existing_record.score = score
                    existing_record.updated_at = datetime.now()
                    existing_record.save()
                    return existing_record
                else:
                    return existing_record
            else:
                new_record = HighScore.create(
                    score=score,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
                print('New Record!!')
                return new_record

        except Exception as e:
            print(f"Fail to update high score: {e}")
            raise