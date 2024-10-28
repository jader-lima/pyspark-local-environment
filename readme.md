# PySpark Local Environment

A Docker-based local environment setup for running PySpark. This repository is intended for data engineers and analysts who need a quick, consistent setup for developing and testing PySpark applications locally. The setup is highly extendable, allowing the addition of other services such as relational or NoSQL databases, message queues, and more.

## Table of Contents

1. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Setup](#setup)
2. [Configuration](#configuration)
3. [How to Run](#how-to-run)
   - [Setting Up Local Environment](#setting-up-local-environment)
   - [Running the Services](#running-the-services)
   - [Accessing the Spark UI](#accessing-the-spark-ui)
4. [Testing PySpark Scripts](#testing-pyspark-scripts)
5. [License](#license)

## Getting Started

### Prerequisites

Ensure you have the following tools installed on your machine:

- **Docker**: [Get Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Get Docker Compose](https://docs.docker.com/compose/install/)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/jader-lima/pyspark-local-environment.git
   cd pyspark-local-environment
   ```

## Configuration

The `docker-compose.yml` file initializes a Spark master and worker node along with additional services to support data analysis and streaming (e.g., Pandas, Kafka).

## How to Run

### Setting Up Local Environment

#### Create Folders for Data and Scripts

```bash
mkdir data
mkdir scripts
```

#### Change Folder Permissions

```bash
chmod -R 777 data
chmod -R 777 scripts
```

### Running the Services

#### Build Custom Spark Image

Navigate to the Docker folder and build the custom Spark image:

```bash
cd docker
docker build -t custom-spark-3.5:latest .
```

#### Start PySpark Environment in Detached Mode

```bash
docker-compose up -d
```

### Accessing the Spark UI

Once all services are up and running, you can access the Spark Master UI to monitor job executions:

- **Spark Master UI**: [http://localhost:8080](http://localhost:8080)

## Testing PySpark Scripts

To test the environment and run sample scripts, follow these steps:

1. **Access the Spark Master Container in Interactive Mode**:

   ```bash
   docker exec -it spark-master bash
   ```

2. **Execute `spark-submit` with a Test Script**:

   Run the `create-dataframe.py` script:

   ```bash
   docker exec -it spark-master spark-submit /opt/spark/scripts/create-dataframe.py
   ```

3. **Execute the Customer Ingestion Script**:

   Run the `customer_ingestion.py` script:

   ```bash
   docker exec -it spark-master spark-submit /opt/spark/scripts/olist/ingestion/customer_ingestion.py
   ```

## License

This project is licensed under the MIT License.
