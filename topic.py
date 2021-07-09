import json
from datetime import datetime

from kafka import KafkaConsumer, KafkaProducer

TEST_TOPIC = 'test.topic'
# KAFKA_SERVER = '10.1.1.51:9092'
KAFKA_SERVER = 'localhost:9092'
TEST_MESSAGE = b'MESSAGE'
TEST_GROUP = 'TEST_GROUP'


def test():
    # consumer = KafkaConsumer(TEST_TOPIC, bootstrap_servers=KAFKA_SERVER, group_id=TEST_GROUP)
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

    future = producer.send(TEST_TOPIC, TEST_MESSAGE)
    record = future.get(timeout=10)
    print(record)

    # message = next(consumer)
    # print(message)
    #
    # assert TEST_MESSAGE == message.value


def gios_installation_created():
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    topic = "gios.installation"
    # timestamp = int(datetime.now().timestamp())
    timestamp = 1604271285
    station = "TestStation"
    key = str(timestamp) + '-' + station
    event = {
        "eventType": "GiosInstallationCreatedEvent",
        "timestamp": timestamp,
        "payload": {
            "installation": {
                "id": "123",
                "name": station,
                "timestamp": timestamp,
                "value": 124.9,
                "lon": 1.0,
                "lat": 1.0,
                "code": "PM10"
            }
        }
    }
    raw_event = json.dumps(event)
    print(raw_event)
    return producer.send(topic, str.encode(raw_event), str.encode(key)).get(timeout=10)


if __name__ == '__main__':
    # test()
    gios_installation_created()
