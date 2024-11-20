### **Building python custom library (`py/`)**

# Custom Kafka Python Library

This directory contains a custom Python library to simplify interactions with Kafka. The library is built using `confluent-kafka` and provides reusable producer and consumer classes.


### Building the Library
To build the custom Python library:

Install the required tools for building a Python package:

```bash
pip install setuptools wheel

```

Navigate to the library's root directory:

```bash
cd py/lib_confluent_kafka_python/

```

Build the library:

```bash
python3 setup.py sdist bdist_wheel

```
The .whl file will be available in the dist/ directory.

### Installing the Library
Install the library in your Python environment:

```bash
The .whl file will be available in the dist/ directory.

```

### Using the Library

## Admin Example
Use the KafkaAdmin class to create, list and delete Kafka topics:

```python
from lib_confluent_kafka_python.KafkaAdmin import KafkaAdmin

broker = "kafka:9092"
topic = "sellers"
group_id = "my_group"



config = {'bootstrap.servers': broker,
        'socket.timeout.ms': 10000,
            'api.version.request': 'true',
        'broker.version.fallback': '0.10.0',
        'enable.idempotence': 'true'  }

kafka_Admin = KafkaAdmin(config )


topic_name = 'sellers'
topic_list = []
topic = kafka_Admin.createTopicElement(topic_name, 3 , 1)
topic_list.append(topic)
kafka_Admin.createTopictoKafka(topic_list) 

kafka_Admin.listKafkaTopics().topics


```

## Producer Example
Use the KafkaProducer class to send messages to a Kafka topic:

```python
from lib_confluent_kafka_python.KafkaAdmin import KafkaAdmin
from lib_confluent_kafka_python.KafkaProducer import KafkaProducer

broker = "kafka:9092"
topic = "sellers"
group_id = "my_group"



config = {'bootstrap.servers': broker,
        'socket.timeout.ms': 10000,
        'api.version.request': 'true',
        'broker.version.fallback': '0.10.0',
        'enable.idempotence': 'true'  }

kafkaProducer = KafkaProducer(config )

message = '{"seller_id":"001cca7ae9ae17fb1caed9dfb1094839","seller_zip_code_prefix":"29156","seller_city":"cariacica","seller_state":"SP"}'

partition_number = None
topic = "sellers"
kafkaProducer.produce_message(topic, msg=message, partition=partition_number)


```


## Consumer Example
Use the KafkaConsumer class to consume messages from a Kafka topic:

```python
from lib_confluent_kafka_python.KafkaConsumer import KafkaConsumer

broker = "kafka:9092"
topic = "sellers"
group_id = "my_group"


broker = "kafka:9092"
topic = "sellers"
group_id = "my_group"

# "auto.offset.reset" : "latest" , "largest", "earliest"

config = {
    'bootstrap.servers': broker,
    'group.id': group_id,
    'socket.timeout.ms': 10000,
    'api.version.request': 'true',
    'broker.version.fallback': '0.10.0',
    'enable.idempotence': 'true',
    'auto.offset.reset': 'latest',
    'enable.auto.commit': 'false',  # Desabilita o auto-commit para controle manual
    'max.poll.interval.ms': '86400000',
    'partition.assignment.strategy': 'range'
    }

kafkaConsumer = KafkaConsumer(config)
consumer = kafkaConsumer.create_consumer()

def consume_messages(kafkaConsumer : KafkaConsumer, topic, partition=None):
    if partition is not None:
        consumer.assign([TopicPartition(topic, partition)])
        print(f"Assigned to partition {partition} of topic '{topic}'")
    else:
        consumer.subscribe([topic])
        print(f"Subscribed to topic '{topic}'")
        
    try:
        while True:
            print("Listening")
            # read single message at a time

            msg = consumer.poll(0)

            if msg is None:
                sleep(5)
                continue
            if msg.error():
                print("Error reading message : {}".format(msg.error()))
                continue
            # You can parse message and save to data base here
            value = msg.value().decode('utf-8')
            print(value)
            print("Partition:", msg.partition(), "Offset:", msg.offset())
            consumer.commit()

    except Exception as ex:
        print("Kafka Exception : {}", ex)

    finally:
        print("closing consumer")
        consumer.close()


partition = None
kafkaConsumer = KafkaConsumer(config)
consumer = kafkaConsumer.create_consumer()
consume_messages(consumer, topic, partition=partition)

```



