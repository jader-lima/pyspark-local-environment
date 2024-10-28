#### create folder's data and scripts
mkdir data
mkdir scripts

#### changing permissions of the folders
chmod -R 777 data
chmod -R 777 scripts

#### starting pyspark environment in detached mode
docker-compose up -d


#### building custom image
cd docker
docker build -t custom-spark-3.5:latest .

#### execute spark-master container in interative mode
docker exec -it spark-master bash

#### execute spark-submit command - script customer_ingestion.py
docker exec -it spark-master spark-submit /opt/spark/scripts/create-dataframe.py

#### execute spark-submit command - script customer_ingestion.py
docker exec -it spark-master spark-submit /opt/spark/scripts/olist/ingestion/customer_ingestion.py




