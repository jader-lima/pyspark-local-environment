# PySpark Local Environment

This repository provides a setup for a local environment to run PySpark scripts, including batch and streaming processing examples. The configuration uses Docker containers to replicate a distributed environment with Apache Spark.

---

## Table of Contents
1. [Setting Up the Local Environment](#1---setting-up-the-local-environment)  
   - [Creating directories](#11---creating-directories)  
   - [Changing directory permissions](#12---changing-directory-permissions)  
   - [Building the custom library](#13---building-the-custom-library)  
2. [Starting the PySpark Environment](#2---starting-the-pyspark-environment)  
   - [Optional interactive mode](#21---optional-interactive-mode)  
3. [Running PySpark Scripts in Batch Mode](#3---running-pyspark-scripts-in-batch-mode)  
4. [Running PySpark Scripts in Streaming Mode](#4---running-pyspark-scripts-in-streaming-mode)  
   - [Preparing data directories](#41---preparing-data-directories)  
   - [Cleaning data and checkpoint directories](#42---cleaning-data-and-checkpoint-directories)  
   - [Running the data generator](#43---running-the-data-generator)  
   - [Running scripts in streaming mode](#44---running-scripts-in-streaming-mode)  
5. [Using the Custom Python Library with PySpark](#5---using-the-custom-python-library-with-pyspark)

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

### 1.3 - Building python custom library
To build the custom Python library:

Navigate to the library's root directory:

```bash
cd py/lib_custom_python/

```

Install the required tools for building a Python package:

```bash
pip install setuptools wheel

```

Build the library:

```bash
python3 setup.py sdist bdist_wheel

```
The generated .whl file will be located in the dist/ directory.
Copy .whl todata/lib folder.


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
