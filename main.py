import logging

from dotenv import load_dotenv

from config.settings import get_config
from notion_archiver import NotionArchiver
from slack_crawler import SlackCrawler

load_dotenv()

def main():

    config = get_config()

    logging.basicConfig(
        filename='../logs/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s: %(message)s'
    )

    try:
        slack_crawler = SlackCrawler(
            bot_token=config['slack']['bot_token'],
            channel_id=config['slack']['channel_id']
        )
        messages = slack_crawler.fetch_messages()

        notion_archiver = NotionArchiver(
            token=config['notion']['token'],
            page_id=config['notion']['page_id']
        )
        notion_archiver.archive_messages(messages)

        logging.info("Slack message archiving completed")

    except Exception as e:
        logging.error(f"Error occurred during archiving: {e}")

if __name__ == "__main__":
    main()