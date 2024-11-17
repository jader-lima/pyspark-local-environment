from confluent_kafka import Consumer

class KafkaConsumer: 
    def __init__(self, conf):
        self.conf = conf        

    def create_consumer(self):
        return Consumer(self.conf)   


if __name__ == "__main__":
    kafkaConsumer = KafkaConsumer()