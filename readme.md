# PySpark Local Environment

This repository provides a setup for a local environment to run PySpark scripts, including batch and streaming processing examples. The configuration uses Docker containers to replicate a distributed environment with Apache Spark.

## Table of Contents
1. [Setting Up the Local Environment](#1---setting-up-the-local-environment)
   - [Creating directories](#11---creating-directories)
   - [Changing directory permissions](#12---changing-directory-permissions)
   - [Building the custom image](#13---building-the-custom-image)
2. [Starting the PySpark Environment](#2---starting-the-pyspark-environment)
   - [Optional interactive mode](#21---optional-interactive-mode)
3. [Running PySpark Scripts in Batch Mode](#3---running-pyspark-scripts-in-batch-mode)
4. [Running PySpark Scripts in Streaming Mode](#4---running-pyspark-scripts-in-streaming-mode)
   - [Preparing data directories](#41---preparing-data-directories)
   - [Cleaning data and checkpoint directories](#42---cleaning-data-and-checkpoint-directories)
   - [Running the data generator](#47---running-the-data-generator)
   - [Running scripts in streaming modes](#48---running-scripts-in-streaming-modes)
5. [Example: Running in Update Mode](#5---example-running-in-update-mode)

---

## 1 - Setting Up the Local Environment

### 1.1 - Creating directories
Create the `data` and `scripts` directories. If they already exist, you can skip this step.
```bash
mkdir data
mkdir scripts
```

### 1.2 - Changing directory permissions
Change the permissions of the directories to allow full access.
```bash
chmod -R 777 data
chmod -R 777 scripts
```

### 1.3 - Building the custom image
Change the permissions of the directories to allow full access.

```bash
cd docker
docker build -t custom-spark-3.5:latest .
```

## 2 - Starting the PySpark Environment
Start the PySpark environment using docker-compose.

```bash
docker-compose up -d
```

### 2.1 - Optional interactive mode
You can run bash commands interactively in the spark-master container.

```bash
docker exec -it spark-master bash
```

```bash
docker exec -it spark-master spark-submit /opt/spark/scripts/test/create-dataframe.py
```

## 3 - Running PySpark Scripts in Batch Mode
Run PySpark batch scripts using spark-submit.

```bash
docker exec -it spark-master spark-submit /opt/spark/scripts/olist/ingestion/customer_ingestion.py
```

## 4 -  Running PySpark Scripts in Streaming Mode
### 4.1 - Preparing data directories
Create directories for storing transient data.

```bash
docker exec -it spark-master bash /opt/spark/scripts/bash/create_folder.sh "/opt/spark/data/transient/product_sales/"
docker exec -it spark-master bash /opt/spark/scripts/bash/create_folder.sh "/opt/spark/data/transient/product_sales_update/"
```

### 4.2 - Cleaning data and checkpoint directories
If the script has been run before, clean the data and checkpoint directories.

```bash
docker exec -it spark-master bash /opt/spark/scripts/bash/delete_folder_files.sh "/opt/spark/data/transient/product_sales/*"
docker exec -it spark-master bash /opt/spark/scripts/bash/delete_folder_files.sh "/opt/spark/data/transient/product_sales_update/*"
docker exec -it spark-master bash /opt/spark/scripts/bash/delete_folder_files.sh "/opt/spark/data/checkpoint/streaming_read_console"
docker exec -it spark-master bash /opt/spark/scripts/bash/delete_folder_files.sh "/opt/spark/data/checkpoint/streaming_read_console_update"

```
### 4.3 - Running scripts in streaming modes
**Append Mode**
Open a new terminal and run the following command:

```bash
docker exec -it spark-master spark-submit /opt/spark/scripts/streaming/streaming_read_append_mode_console.py \
--transient_path "/opt/spark/data/transient/product_sales/"

```
**Complete Mode**
Open a new terminal and run the following command:

```bash
docker exec -it spark-master spark-submit /opt/spark/scripts/streaming/streaming_read_complete_mode_console.py \
--transient_path "/opt/spark/data/transient/product_sales/" \
--checkpoint_path "/opt/spark/data/checkpoint/streaming_read_console"

```
## 5 -  Example: Running in Update Mode
### 5.1 - Running scripts in streaming modes
**Update Mode**

```bash
docker exec -it spark-master spark-submit /opt/spark/scripts/streaming/streaming_read_update_mode_console.py \
--transient_path "/opt/spark/data/transient/product_sales_update/" \
--checkpoint_path "/opt/spark/data/checkpoint/streaming_read_console_update"
```

### 5.2 - Copying files to transient directories
Open a new terminal and run these commands one by one, waiting at least 10 seconds between each to observe the results:

```bash
docker exec -it spark-master cp /opt/spark/data/update_files/product_sales1.csv /opt/spark/data/transient/product_sales_update/product_sales1.csv
docker exec -it spark-master cp /opt/spark/data/update_files/product_sales2.csv /opt/spark/data/transient/product_sales_update/product_sales2.csv
docker exec -it spark-master cp /opt/spark/data/update_files/product_sales3.csv /opt/spark/data/transient/product_sales_update/product_sales3.csv
docker exec -it spark-master cp /opt/spark/data/update_files/product_sales4.csv /opt/spark/data/transient/product_sales_update/product_sales4.csv

```

/opt/bitnami/kafka/bin

### 5.2 - create kafka topic
docker exec -it kafka bash

/opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server kafka:9092 \
--create \
--topic test-topic \
--replication-factor 1 \
--partitions 3


/opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server kafka:9092 --list



/opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server kafka:9092 --describe --topic test-topic




### create messages
/opt/bitnami/kafka/bin/kafka-console-producer.sh --bootstrap-server kafka:9092 \
--topic test-topic

### consume messages
/opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 \
--topic test-topic \
--from-beginning


mkdir -p zookeeper/data zookeeper/datalog  kafka
chmod -R 777 zookeeper kafka




version: "3.8"

services:
  master:
    image: custom-spark-3.5:latest #docker.io/bitnami/spark:3.5
    container_name: spark-master
    hostname: master
    environment:
      - SPARK_MODE=master
      - SPARK_RPC_AUTHENTICATION_ENABLED=no
      - SPARK_RPC_ENCRYPTION_ENABLED=no
      - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
      - SPARK_SSL_ENABLED=no
      - SPARK_USER=spark
      - SPARK_LOG_CONF=/opt/bitnami/spark/conf/log4j2.properties
      - PYTHONPATH=/opt/bitnami/spark/jobs/app:/opt/bitnami/spark/jobs/app/
    ports:
      - "8080:8080"
      - "7077:7077"
    volumes:
      - ./scripts:/opt/spark/scripts
      - ./data:/opt/spark/data

  worker1:
    image: custom-spark-3.5:latest #docker.io/bitnami/spark:3.5
    container_name: spark-worker-1
    hostname: worker1
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER_URL=spark://spark-master:7077
      - SPARK_WORKER_MEMORY=1G
      - SPARK_WORKER_CORES=2
      - SPARK_RPC_AUTHENTICATION_ENABLED=no
      - SPARK_RPC_ENCRYPTION_ENABLED=no
      - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
      - SPARK_SSL_ENABLED=no
      - SPARK_USER=spark
      - SPARK_LOG_CONF=/opt/bitnami/spark/conf/log4j2.properties
    volumes:
      - ./scripts:/opt/spark/scripts
      - ./data:/opt/spark/data
    depends_on:
      - master

  worker2:
    image: custom-spark-3.5:latest #docker.io/bitnami/spark:3.5
    container_name: spark-worker-2
    hostname: worker2
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER_URL=spark://spark-master:7077
      - SPARK_WORKER_MEMORY=1G
      - SPARK_WORKER_CORES=2
      - SPARK_RPC_AUTHENTICATION_ENABLED=no
      - SPARK_RPC_ENCRYPTION_ENABLED=no
      - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
      - SPARK_SSL_ENABLED=no
      - SPARK_USER=spark
      - SPARK_LOG_CONF=/opt/bitnami/spark/conf/log4j2.properties
    volumes:
      - ./scripts:/opt/spark/scripts
      - ./data:/opt/spark/data
    depends_on:
      - master

  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    hostname: zookeeper
    container_name: zookeeper
    ports:
      - "2181:2181"
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    volumes:
      - ./zookeeper/data:/data
      - ./zookeeper/datalog:/datalog

  kafka:
    image: confluentinc/cp-kafka:latest
    hostname: kafka
    container_name: kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      restart: always
    volumes:
      - ./zookeeper/kafka/data:/var/lib/kafka/data
    depends_on:
      - zookeeper

  jupyter:
    image: jupyter/datascience-notebook:python-3.8.4
    container_name: jupyter
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/mnt/notebooks:rw
      - ./data/:/mnt/data:rw
      - ./py/:/mnt/py:rw
    environment:
      JUPYTER_ENABLE_LAB: "yes"
    command: "start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''"



