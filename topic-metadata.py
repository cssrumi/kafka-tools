from kafka import KafkaConsumer

consumer = KafkaConsumer(group_id='test', bootstrap_servers=['localhost:9092'])
[print(topic, consumer.partitions_for_topic(topic)) for topic in consumer.topics()]
