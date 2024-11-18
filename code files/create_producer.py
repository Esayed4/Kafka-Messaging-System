from kafka import KafkaProducer
bootstrap_server='localhost:9092'
topic_name='practice'

def send_message(bootstrap_server, topic_name, key, value):
    producer=KafkaProducer(bootstrap_servers=bootstrap_server)
    producer.send(topic=topic_name, key=key, value=value)
    producer.flush()

while(1):
    key,value=input('enter').split(':')
    if(key=="11"):
        i=0
        str1=f"{i}"
        send_message(bootstrap_server, topic_name,str1.encode('utf-8'),"close".encode('utf-8'))
        str1=f"{i+1}"
        send_message(bootstrap_server, topic_name,str1.encode('utf-8'),"close".encode('utf-8'))
        str1=f"{i+2}"
        send_message(bootstrap_server, topic_name,str1.encode('utf-8'),"close".encode('utf-8'))
        
    send_message(bootstrap_server, topic_name,key=key.encode('utf-8'),value=value.encode('utf-8'))


