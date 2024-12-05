import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackCrawler:
    def __init__(self, bot_token, channel_id):
        self.client = WebClient(token=bot_token)
        self.channel_id = channel_id

    def fetch_messages(self, limit=100):
        try:
            response = self.client.conversations_history(
                channel=self.channel_id,
                limit=limit
            )

            messages = [{
                'text': msg.get('text', ''),
                'user': msg.get('user', ''),
                'timestamp': msg.get('ts', ''),
                'attachments': msg.get('attachments', [])
            } for msg in response.get('messages', [])]

            logging.info(f"{len(messages)}개 메시지를 추출했어요.")
            return messages

        except SlackApiError as e:
            logging.error(f"API Error: {e}")
            return []