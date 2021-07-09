import json
from collections import defaultdict

from kafka import KafkaConsumer

# KAFKA_SERVER = '10.1.1.51:9092'
KAFKA_SERVER = 'localhost:9092'

consumer = KafkaConsumer(bootstrap_servers=KAFKA_SERVER, group_id='TEST_3')
consumer.subscribe(pattern='test.radon.measurements')
# consumer.subscribe(pattern='update.gios.measurement')

message_stats = defaultdict(int)

for msg in consumer:
    event = json.loads(msg.value)
    message_stats[event.get('eventType')] += 1
    print("event:", event, ", key: %s", msg.key, ", stats: ", message_stats)
