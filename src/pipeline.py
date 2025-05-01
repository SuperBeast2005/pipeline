from quixstreams import Application
import logging

app = Application(
    broker_address="publickafka.quix.io:9092",
    loglevel="DEBUG"
    )

with app.get_producer() as producer:
    producer.produce(
        topic = "test"
    )
    
def main():
    logging.info("STARTING")
    
if __name__=="__main__":
    logging.basicConfig(level="DEBUG")
    main()