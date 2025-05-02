from kafka import KafkaProducer
import json
from data_gen import generate_random_data

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def produce():
    topic = 'json-data-stream'
    while True:    
        data = generate_random_data()
        producer.send(topic, value=data)
        print(f"Produced: {data}")

if __name__=="__main__":
    produce()