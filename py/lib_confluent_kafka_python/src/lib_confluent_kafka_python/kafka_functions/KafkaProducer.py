from confluent_kafka import Producer
import json
import time


class KafkaProducer:
    kafka_producer = None

    def __init__(self, conf): 
        self.conf = conf
        self.kafka_producer = Producer(self.conf)

    def delivery_callback(self, err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))

    def produce_message(self, topic, msg, key=None, partition=None):
        self.topic = topic
        print("Send message asynchronously")
        self.kafka_producer.produce(
            self.topic,
            value=msg, 
            key=key,
            partition=partition,
            callback=self.delivery_callback
        )        
        
        self.kafka_producer.flush()



if __name__ == "__main__":
    kafkaProducer = KafkaProducer()