import logging
from datetime import datetime

from notion_client import Client


class NotionArchiver:
    def __init__(self, token, page_id):
        self.client = Client(auth=token)
        self.page_id = page_id

    def archive_messages(self, messages):
        try:
            blocks = []
            for msg in messages:
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": f"From: {msg['user']}\n{msg['text']}"
                                }
                            }
                        ]
                    }
                })
                
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": f"Sent at: {datetime.fromtimestamp(float(msg['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')}"
                                },
                                "annotations": {
                                    "italic": True,
                                    "color": "gray"
                                }
                            }
                        ]
                    }
                })

                blocks.append({
                    "object": "block",
                    "type": "divider",
                    "divider": {}
                })

            self.client.blocks.children.append(
                block_id=self.page_id,
                children=blocks
            )
            
            logging.info(f"Archived {len(messages)} messages to page")

        except Exception as e:
            logging.error(f"Archiving Error: {e}")