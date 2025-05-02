from kafka import KafkaConsumer
import json
from transformer import transform
from pymongo import MongoClient
import logging
import time
import multiprocessing

client = MongoClient("mongodb://localhost:27017/")

def consume():
    consumer = KafkaConsumer(
        'json-data-stream',
        bootstrap_servers='localhost:9092',
        #turns loaded bytes from JSON into python dictionary object
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='etl-consumer-group'
    )
    
    logging.info("Creating database!")
    db = client["data_user"]
    
    logging.info("Creating collection!")
    collection = db["transformed_data"]

    logging.info("Starting etl-consumer...")
    for message in consumer:
        raw_data = message.value
        logging.info(f"Raw data: {raw_data}")
        transformed_data = transform(raw_data)
        logging.info("Inserting transformed data")
        collection.insert_one(transformed_data)
        logging.info(f"Inserted data:{transformed_data}")

if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    try:
        p = multiprocessing.Process(target=consume)
        p.start()
        time.sleep(5*60)
        p.terminate()
        p.join()
    except Exception as e:
        print(e)
        
 
        