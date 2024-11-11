import confluent_kafka.admin
import json
import time

import confluent_kafka.admin, pprint
from confluent_kafka import KafkaError


class KafkaAdmin:
    def __init__(self, conf):        
        self.conf = conf
        self.kafkaAdmin = confluent_kafka.admin.AdminClient(self.conf)

    def createTopictoKafka(self, topic ):             
        self.kafkaAdmin.create_topics(topic) 

    def deleteTopics(self, topic_list : list ):             
        self.kafkaAdmin.delete_topics(topic_list) 

    def createTopicElement(self, topic , par1, par2 ):             
        return confluent_kafka.admin.NewTopic(topic, par1, par2)
    
    def listKafkaTopics(self ):             
        return self.kafkaAdmin.list_topics()


        

if __name__ == "__main__":
    kafkaAdmin = KafkaAdmin()