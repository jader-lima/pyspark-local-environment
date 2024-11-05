# Building local environment 
## 1 - creating  folders

### 1.1 - create folder's data and scripts , if it exists, ignore it
mkdir data
mkdir scripts

### 1.2 - changing permissions of the folders
chmod -R 777 data
chmod -R 777 scripts

### 1.3 building custom image
cd docker
docker build -t custom-spark-3.5:latest .

## 2 starting pyspark environment
docker-compose up -d

### 2. 1 -  execute spark-master container in interative mode optinal
Could be usefull to run bash command in pyspark master container

docker exec -it spark-master bash BASH_COMMAND OR SH SCRIPT

## 3 - Running pyspark scripts with spark-submit - batch script

### 3. 1 -  execute spark batch ingestions example
docker exec -it spark-master spark-submit /opt/spark/scripts/olist/ingestion/customer_ingestion.py


## 4 -  Running pyspark scripts with spark-submit - streaming script 


### 4.1 - creating product sales folder
docker exec -it spark-master bash /opt/spark/scripts/bash/create_folder.sh "/opt/spark/data/transient/product_sales/"

### 4.2 - creating product sales folder
docker exec -it spark-master bash /opt/spark/scripts/bash/create_folder.sh "/opt/spark/data/transient/product_sales_update/"

### 4.3 - cleaning transient folder - product sales - If script has been run previously, clean the transient folder
docker exec -it spark-master bash /opt/spark/scripts/bash/delete_folder_files.sh "/opt/spark/data/transient/product_sales/*"

### 4.4 - cleaning transient folder - product sales update - If script has been run previously, clean the transient folder
docker exec -it spark-master bash /opt/spark/scripts/bash/delete_folder_files.sh "/opt/spark/data/transient/product_sales_update/*"

### 4.5 - cleaning checkpoint folder - If script has been run previously, clean the checkpoint folder
docker exec -it spark-master bash /opt/spark/scripts/bash/delete_folder_files.sh "/opt/spark/data/checkpoint/streaming_read_console"

### 4.6 - cleaning checkpoint folder - If script has been run previously, clean the checkpoint folder
docker exec -it spark-master bash /opt/spark/scripts/bash/delete_folder_files.sh "/opt/spark/data/checkpoint/streaming_read_console_update"


### 4.7 - execute data generator file
docker exec -it spark-master python /opt/spark/scripts/data_generator/data_generator.py --output_path "/opt/spark/data/transient/product_sales/" --number 50


### 4.8 - execute spark streaming append mode console example

Open a new terminal and run the above command

docker exec -it spark-master spark-submit /opt/spark/scripts/streaming/streaming_read_append_mode_console.py \
--transient_path "/opt/spark/data/transient/product_sales/" 

### 4.9 - execute spark streaming complete mode console example

Open a new terminal and run the above command

docker exec -it spark-master spark-submit /opt/spark/scripts/streaming/streaming_read_complete_mode_console.py \
--transient_path "/opt/spark/data/transient/product_sales/" \
--checkpoint_path "/opt/spark/data/checkpoint/streaming_read_console"

### 5 execute spark streaming update mode console example

### 5.1 - execute spark streaming update mode console example

Open a new terminal and run the above command

docker exec -it spark-master spark-submit /opt/spark/scripts/streaming/streaming_read_update_mode_console.py \
--transient_path "/opt/spark/data/transient/product_sales_update/" \
--checkpoint_path "/opt/spark/data/checkpoint/streaming_read_console_update"


### 5.2 - open a new terminal windows and execute copy commands, waiting at least 10 seconds to execute next command

Open a new terminal and run the above command

docker exec -it spark-master cp /opt/spark/data/update_files/product_sales1.csv /opt/spark/data/transient/product_sales_update/product_sales1.csv 

docker exec -it spark-master cp /opt/spark/data/update_files/product_sales2.csv /opt/spark/data/transient/product_sales_update/product_sales2.csv 

docker exec -it spark-master cp /opt/spark/data/update_files/product_sales3.csv /opt/spark/data/transient/product_sales_update/product_sales3.csv 

docker exec -it spark-master cp /opt/spark/data/update_files/product_sales4.csv /opt/spark/data/transient/product_sales_update/product_sales4.csv 






