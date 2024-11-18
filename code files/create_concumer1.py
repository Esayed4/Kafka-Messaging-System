from kafka import KafkaConsumer

def read(bootstrap_server, topic_name):
    conumer=KafkaConsumer(topic_name, bootstrap_servers=bootstrap_server,group_id='g')
    for line in conumer :
        value=line.value.decode('utf-8')
        key=line.key.decode('utf-8')
        if(key=="11"):
            print("you kill me")
            break
        print(value)
        
    conumer.close()


bootstrap_server='localhost:9092'
topic_name='practice'
read(bootstrap_server,topic_name)