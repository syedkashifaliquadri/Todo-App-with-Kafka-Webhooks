from confluent_kafka import Consumer, KafkaError
import config
import requests


def send_to_webhook(event_key, event_value):
    webhook_url = config.WEBHOOK_URL
    response = requests.post(webhook_url, json={"event_key": event_key, "event_value": event_value})
    print("Webhook status:", response.status_code)
    if response.status_code == 200:
        print("Webhook response:", response.text)


class KafkaConsumer:
    def __init__(self):
        self.consumer = Consumer({
            "bootstrap.servers": config.KAFKA_BOOTSTRAP_SERVERS,
            "group.id": "my-consumer-group",
            "auto.offset.reset": "earliest"
        })
        self.consumer.subscribe([config.KAFKA_TOPIC])

    def consume_events(self):
        while True:
            try:
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
                    if msg.key() and msg.value():
                        event_key = msg.key().decode("utf-8")
                        event_value = msg.value().decode("utf-8")
                        send_to_webhook(event_key, event_value)
            except Exception as e:
                print(f"Error while consuming: {e}")
