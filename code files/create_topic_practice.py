from kafka import KafkaAdminClient
from kafka.admin import NewTopic

bootstrap_server='localhost:9092'
topic_name='practice'
partitions=3


admin=KafkaAdminClient(bootstrap_servers=bootstrap_server)
new_topic=NewTopic(name= topic_name, num_partitions= partitions, replication_factor=1)
topic_list=[new_topic]
admin.create_topics(new_topics=topic_list)
