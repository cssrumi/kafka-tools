from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id='kafka-tools'
)

topic = "update.gios.measurement"
topic_list = [NewTopic(name=topic, num_partitions=3, replication_factor=1)]
# admin_client.delete_topics(topics=[topic])
admin_client.create_topics(new_topics=topic_list, validate_only=False)
