import logging
from notion_client import Client
from datetime import datetime

class NotionArchiver:
    def __init__(self, token, database_id):
        self.client = Client(auth=token)
        self.database_id = database_id

    def archive_messages(self, messages):
        for msg in messages:
            try:
                self.client.pages.create(
                    parent={'database_id': self.database_id},
                    properties={
                        'Message': {
                            'rich_text': [{'text': {'content': msg['text']}}]
                        },
                        'User': {
                            'rich_text': [{'text': {'content': msg['user']}}]
                        },
                        'Timestamp': {
                            'date': {
                                'start': datetime.fromtimestamp(float(msg['timestamp'])).isoformat()
                            }
                        }
                    }
                )
                logging.info(f"Archived Message: {msg['text'][:50]}...")

            except Exception as e:
                logging.error(f"Archiving Error: {e}")