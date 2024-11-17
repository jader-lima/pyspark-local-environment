import confluent_kafka.admin
import json
import time

import confluent_kafka.admin, pprint
from confluent_kafka import KafkaError


class KafkaAdmin:
    def __init__(self, conf):        
        self.conf = conf
        self.kafkaAdmin = confluent_kafka.admin.AdminClient(self.conf)

    def createTopictoKafka(self, topic_list):
        futures = self.kafkaAdmin.create_topics(topic_list)
        for topic, future in futures.items():
            try:
                future.result() 
                print(f"Topic '{topic}' created successfully.")
            except KafkaError as e:
                print(f"Error creating topic'{topic}': {e}")

    def deleteTopics(self, topic_list):
        futures = self.kafkaAdmin.delete_topics(topic_list, operation_timeout=30)
        for topic, future in futures.items():
            try:
                future.result()  
                print(f"Topic '{topic}' deleted successfully.")
            except KafkaError as e:
                print(f"Error deleting topic '{topic}': {e}")

    def createTopicElement(self, topic , par1, par2 ):             
        return confluent_kafka.admin.NewTopic(topic, par1, par2)
    
    def listKafkaTopics(self ):             
        return self.kafkaAdmin.list_topics()


        

if __name__ == "__main__":
    kafkaAdmin = KafkaAdmin()






