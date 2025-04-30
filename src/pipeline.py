from quixstreams import Application

app = Application(
    broker_address="publickafka.quix.io:9092",
    loglevel="DEBUG"
    )

with app.get_producer() as producer:
    producer.produce(
        topic = "test"
    )