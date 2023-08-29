from confluent_kafka import Producer
import config


class KafkaProducer:
    def __init__(self):
        self.producer = Producer({"bootstrap.servers": config.KAFKA_BOOTSTRAP_SERVERS})

    def send_event(self, event_key, event_value):
        self.producer.produce(config.KAFKA_TOPIC, key=event_key, value=event_value)
        self.producer.flush()
