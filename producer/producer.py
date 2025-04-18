import logging
import time
import os
import json
import requests
from config.settings import COINLORE_API_URL, TOPIC_INPUT, FETCH_INTERVAL
from quixstreams import Application



def fetch_data():
    """Fetches the BTC data"""
    try:
        response = requests.get(COINLORE_API_URL)
        data = response.json()
        logging.info("Data fetched successfully!")
        return json.dumps(data[0])
    except Exception as e:
        logging.error(f"API fetch failed: {e}")
        return None

def main():

    app = Application(
        broker_address = 'redpanda:9092',
        loglevel = 'INFO'
    )

    while True:
        data = fetch_data()
        if data:
            with app.get_producer() as producer:
                producer.produce(
                    topic = TOPIC_INPUT,
                    key = 'BTC',
                    value = data
                )
                logging.info('Data produced.')
        time.sleep(FETCH_INTERVAL)
        



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()



