from kafka import KafkaConsumer
import json
from transformer import transform
import psycopg2
import logging
import time
import multiprocessing

conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="data_user",
    user="postgres",
    password="alexander2005"
)

cursor = conn.cursor()

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
    
    logging.info("Creating table!")
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS transformed_data (
            id INTEGER NOT NULL,
            full_name TEXT NOT NULL,
            birthdate TEXT NOT NULL,
            full_ip TEXT NOT NULL);
        """)

    logging.info("Starting etl-consumer...")
    for message in consumer:
        raw_data = message.value
        logging.info(f"Raw data: {raw_data}")
        transformed_data = transform(raw_data)
        logging.info("Inserting transformed data")
        cursor.execute(""" 
            INSERT INTO transformed_data (id, full_name, birthdate, full_ip)
            VALUES (%s, %s, %s, %s)""", (
                transformed_data['id'],
                transformed_data['full_name'],
                transformed_data['birthdate'],
                transformed_data['full_ip']    
            )
            )
        logging.info(f"Inserted data:{transformed_data}")
        #time.sleep(1)
        conn.commit()
    conn.close()
    logging.info(f"Database-Connection closed!")
 
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
        