COINLORE_API_URL = "https://api.coinlore.net/api/ticker/?id=90"
FETCH_INTERVAL = 15 

KAFKA_BROKER_ADDRESS = "localhost:9092"  
TOPIC_INPUT = "crypto_prices"
CONSUMER_GROUP = "crypto_analytics"
TOPIC_OUTPUT = "transformed_crypto_prices"

WINDOW_SIZE = 5  # Number of data points for moving average
