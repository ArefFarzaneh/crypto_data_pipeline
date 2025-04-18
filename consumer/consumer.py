from quixstreams import Application
import logging
from config.settings import KAFKA_BROKER_ADDRESS, TOPIC_INPUT, TOPIC_OUTPUT, CONSUMER_GROUP, WINDOW_SIZE
import json
import pandas as pd
from collections import deque
import os

symbol_windows = {} 

def transform(msg):
    """Transformation logic, calculating moving average"""
    if msg is not None:
        symbol = msg['symbol']
        price = msg['price_usd']
        if symbol not in symbol_windows:
            symbol_windows[symbol] = deque(maxlen=WINDOW_SIZE)
        
        symbol_windows[symbol].append(float(price))
        
        if len(symbol_windows[symbol]) == WINDOW_SIZE:
            print(symbol_windows[symbol])
            moving_average = sum(symbol_windows[symbol]) / WINDOW_SIZE
        else:
            moving_average = ""

        data = {
                'symbol': symbol,
                'price': price,
                'moving_average': moving_average,
                'window_size': WINDOW_SIZE,
                'timestamp': pd.Timestamp.now().isoformat()
            }
        logging.debug(f"Transformed: {msg}")
        return data
    else:
        logging.debug(f"None message!")
        return None

def main():
    """Continuously consume, transform, and produce to new topic."""

    app = Application(
        broker_address='redpanda:9092',
        consumer_group=CONSUMER_GROUP,
        auto_offset_reset="latest",  
    )
    
    input_topic = app.topic(TOPIC_INPUT, value_deserializer="json")
    output_topic = app.topic(TOPIC_OUTPUT, value_deserializer="json")
    
    sdf = app.dataframe(input_topic)
    sdf = sdf.apply(transform)
    sdf = sdf.to_topic(output_topic)
    
    logging.info("Starting consumer...")
    app.run(sdf)  

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()