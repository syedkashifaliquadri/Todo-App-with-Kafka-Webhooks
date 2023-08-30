from confluent_kafka import Consumer, KafkaError
import config
import requests

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "todo"
WEBHOOK_URL = "http://localhost:5000/api/webhook"


class KafkaConsumer:
    def __init__(self):
        self.consumer = Consumer({
            "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
            "group.id": "my-consumer-group",
            "auto.offset.reset": "earliest"
        })
        self.consumer.subscribe([KAFKA_TOPIC])

    def consume_events(self):
        while True:
            msg = self.consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
            else:
                print('Received message: {}'.format(msg.value().decode('utf-8')))
                event_key = msg.key().decode("utf-8")
                event_value = msg.value().decode("utf-8")
                self.send_to_webhook(event_key, event_value)

    def send_to_webhook(self, event_key, event_value):
        webhook_url = WEBHOOK_URL
        response = requests.post(webhook_url, json={"event_key": event_key, "event_value": event_value})
        print("Webhook response:", response.status_code)


if __name__ == '__main__':
    consumer = KafkaConsumer()
    consumer.consume_events()
