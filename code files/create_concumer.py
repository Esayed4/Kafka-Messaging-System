from kafka import KafkaConsumer

def read(bootstrap_server, topic_name):
    conumer=KafkaConsumer(topic_name, bootstrap_servers=bootstrap_server,group_id='g')
    for line in conumer :
        value=line.value.decode('utf-8')
        if(line.key=="11".encode('utf-8')):
            print("you kill me")
            break
        print(value,"hi")

    conumer.close()


bootstrap_server='localhost:9092'
topic_name='practice'
read(bootstrap_server,topic_name)