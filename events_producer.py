import json
import time
import random
from kafka import KafkaProducer
from kafka_config import KAFKA_BROKER, TOPIC

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

EVENTS = ["signup", "login", "click", "purchase", "logout"]
FEATURES = ["search", "checkout", "feed", "recommendation"]

while True:
    event = {
        "user_id": random.randint(1, 1000),
        "event_type": random.choice(EVENTS),
        "feature": random.choice(FEATURES),
        "timestamp": time.time()
    }
    producer.send(TOPIC, event)
    print("Sent:", event)
    time.sleep(1)
