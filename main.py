import logging
from dotenv import load_dotenv
from slack_crawler import SlackCrawler
from notion_migrator import NotionMigrator
from config.settings import get_config

def main():
    # 환경설정 및 로깅 초기화
    load_dotenv()
    config = get_config()

    logging.basicConfig(
        filename='../logs/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s: %(message)s'
    )

    try:
        # Slack 메시지 크롤링
        slack_crawler = SlackCrawler(
            bot_token=config['slack']['bot_token'],
            channel_id=config['slack']['channel_id']
        )
        messages = slack_crawler.fetch_messages()

        # Notion으로 마이그레이션
        notion_migrator = NotionMigrator(
            token=config['notion']['token'],
            database_id=config['notion']['database_id']
        )
        notion_migrator.migrate_messages(messages)

        logging.info("Slack message archiving completed")

    except Exception as e:
        logging.error(f"Error occurred during archiving: {e}")

if __name__ == "__main__":
    main()