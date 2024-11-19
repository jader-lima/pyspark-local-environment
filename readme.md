# PySpark Local Environment


## Table of Contents


## 1 - Setting Up the Local Environment



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





### 1.1 - Creating directories
Create the `zookeeper` and `kafka` directories. If they already exist, you can skip this step.
```bash
sudo rm -R  ./zookeeper ./kafka
sudo mkdir -p ./zookeeper/data ./zookeeper/log ./kafka/data
```

### 1.2 - Changing directory permissions
Change the permissions of the directories to allow full access.
```bash

sudo chmod -R 777 ./zookeeper ./kafka
sudo chown -R 1001:1001 ./zookeeper ./kafka
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






