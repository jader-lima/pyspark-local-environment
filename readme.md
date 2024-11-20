# PySpark Local Environment with Kafka Integration

This repository provides a local environment for experimenting with Apache Kafka and custom Python libraries. The setup includes Dockerized services for Kafka, Zookeeper, Kafka UI, and a Jupyter Notebook environment with a custom library to interact with Kafka topics.

## Table of Contents
1. [Purpose](#1-purpose)
2. [Folder Structure](#2-folder-structure)
3. [Environment Setup](#3-environment-setup)
   - [3.1 Prerequisites](#31-prerequisites)
   - [3.2 Creating Directories](#32-creating-directories)
   - [3.3 Changing Directory Permissions](#33-changing-directory-permissions)
   - [3.4 Starting the Environment](#34-starting-the-environment)
   - [3.5 Accessing Jupyter Notebook](#35-accessing-jupyter-notebook)
   - [3.6 Viewing Kafka UI](#36-viewing-kafka-ui)
4. [Custom Python Library](#4-custom-python-library)
5. [Custom Docker Image](#5-custom-docker-image)
6. [Kafka Operations](#6-kafka-operations)
   - [6.1 Managing Topics](#61-managing-topics)
   - [6.2 Producing Messages](#62-producing-messages)
   - [6.3 Consuming Messages](#63-consuming-messages)

---

## 1. Purpose

The project enables users to:
1. Set up a local Kafka environment.
2. Use Jupyter Notebooks to interact with Kafka topics.
3. Create, produce, and consume messages using a custom Python library built on `confluent-kafka`.

---

## 2. Folder Structure

- **data/**: Directory for CSV files or other resources.
- **docker/**: Contains Dockerfiles, including the custom Jupyter Notebook image.
- **notebooks/**: Jupyter Notebooks demonstrating Kafka interactions.
- **py/**: Directory for the custom Python library.

---

## 3. Environment Setup

### 3.1. Prerequisites

Ensure Docker and Docker Compose are installed on your machine.

### 3.2. Creating Directories

Create the `zookeeper` and `kafka` directories. If they already exist, you can skip this step:

```bash
sudo rm -R ./zookeeper ./kafka
sudo mkdir -p ./zookeeper/data ./zookeeper/log ./kafka/data
```

#################


### 3.3. Changing Directory Permissions

Change the permissions of the directories to allow full access. Kafka and Zookeeper need the correct permissions for proper functioning:

```bash
sudo chmod -R 777 ./zookeeper ./kafka
sudo chown -R 1001:1001 ./zookeeper ./kafka
```

### 3.4. Starting the Environment

Run the following command to start all services:

bash
Copiar código

```bash
docker-compose up -d

```

### 3.5. Accessing Jupyter Notebook

After starting the environment, access the Jupyter Notebook UI via:

**http://localhost:8888**


### 3.6. Viewing Kafka UI

Access the Kafka UI via **http://localhost:8889**.
With the graphical interface, you can create, delete, and list Kafka topics, as well as check consumers, partitions, and other characteristics of topics and the Kafka broker.

## 4 - Custom Python Library


## 5 - Custom Docker Image



## 6 - Kafka Operations

### 6.1 - Managing Topics - Create, List and Delete
The notebook Kafkaadmin.ipynb includes examples to:

* Create topics
* List existing topics
* Delete topics

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

### 6.2 - Producing Messages

The notebook KafkaProducer.ipynb demonstrates how to send messages to Kafka topics using the custom library.

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

### 6.3 - Consuming Messages

The notebook KafkaConsumer.ipynb illustrates how to consume messages from Kafka topics using the custom library.

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









###############





## 1 - Environment Setup

### 1.1 - Prerequisites
Ensure Docker and Docker Compose are installed on your machine.


## 2 - Custom Python Library
To build the custom Python library:

Navigate to the library's root directory:

```bash
cd py/lib_confluent_kafka_python/

```

Install the required tools for building a Python package:

```bash
pip install setuptools wheel

```

Build the library:

```bash
python3 setup.py sdist bdist_wheel

```

## 3 - Custom Docker Image
To facilitate the process of building the Docker image, copy the lib_confluent_kafka_python-0.1.0-py3-none-any.whl 
file from the **py/lib_confluent_kafka_python directory** to **docker/custom-jupyter** .

**Important**
If the lib has been updated, build the lib again, replace the old file with the new one and build the docker image again.

Navigate to the docker image directory:

```bash
cd docker/custom-jupyter
docker build -t custom-spark-3.5:latest .
```

### 1.1 - Creating directories 
Create the `zookeeper` and `kafka` directories. If they already exist, you can skip this step.
```bash
sudo rm -R  ./zookeeper ./kafka
sudo mkdir -p ./zookeeper/data ./zookeeper/log ./kafka/data
```

### 1.2 - Changing directory permissions
Change the permissions of the directories to allow full access.
Kafka and zookeeper need the correct permissions for perfect functioning
```bash

sudo chmod -R 777 ./zookeeper ./kafka
sudo chown -R 1001:1001 ./zookeeper ./kafka
```

### 1.3 - Building the custom image
Change the permissions of the directories to allow full access.

### 1.2 - Starting the Environment
Run the following command to start all services:
```bash
docker-compose up -d
```

### 1.3 - Accessing Jupyter Notebook
After starting the environment, access the Jupyter Notebook UI via:
**http://localhost:8888**

### 1.3 - Viewing Kafka UI
After starting the environment, access the Access the Kafka UI via:
It is possible to create, delete and list Kafka topics with the graphical interface, in addition to checking consumers, partitions and other characteristics of topics and the Kafka broker

**http://localhost:8889**


## 6 - Kafka Operations

### 6.1 - Managing Topics - Create, List and Delete
The notebook Kafkaadmin.ipynb includes examples to:

* Create topics
* List existing topics
* Delete topics

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

### 6.2 - Producing Messages

The notebook KafkaProducer.ipynb demonstrates how to send messages to Kafka topics using the custom library.

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

### 6.3 - Consuming Messages

The notebook KafkaConsumer.ipynb illustrates how to consume messages from Kafka topics using the custom library.

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












