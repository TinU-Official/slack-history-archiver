import os

def get_config():
    return {
        'slack': {
            'bot_token': os.getenv('SLACK_BOT_TOKEN'),
            'channel_id': os.getenv('SLACK_CHANNEL_ID')
        },
        'notion': {
            'token': os.getenv('NOTION_TOKEN'),
            'page_id': os.getenv('NOTION_PAGE_ID')
        }
    }