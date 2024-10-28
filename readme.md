#### create folder's data and scripts
mkdir data
mkdir scripts

#### changing permissions of the folders
chmod -R 777 data
chmod -R 777 scripts

#### starting pyspark environment
docker-compose up -d


#### building custom image
cd docker
docker build -t custom-spark-3.5:latest .

#### execute spark-master container in interative mode
docker exec -it spark-master bash

#### execute spark-submit command - script customer_ingestion.py
docker exec -it spark-master spark-submit /opt/spark/scripts/olist/ingestion/customer_ingestion.py


##### executando data generator file
python generate_product_data.py --output_path "/opt/spark/data/transient/product_sales/" --number 50


docker exec -it spark-master python /opt/spark/scripts/data_generator.py --output_path "/opt/spark/data/transient/product_sales/" --number 50




