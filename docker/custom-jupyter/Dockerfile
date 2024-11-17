# BASE IMAGE
FROM jupyter/datascience-notebook:python-3.8.4

# Workdir folder
WORKDIR /home/jovyan/work

# Copy whl file to docker imagem
COPY lib_confluent_kafka_python-0.1.0-py3-none-any.whl /home/jovyan/work/lib_confluent_kafka_python-0.1.0-py3-none-any.whl

# Install whl file using pip
RUN pip install /home/jovyan/work/lib_confluent_kafka_python-0.1.0-py3-none-any.whl && \
    rm /home/jovyan/work/lib_confluent_kafka_python-0.1.0-py3-none-any.whl

# (Opcional) Copie outros arquivos do seu projeto para o contêiner
# COPY . /home/jovyan/work

# (Opcional) Defina comandos padrão, portas expostas, etc.
# EXPOSE 8888
# CMD ["start-notebook.sh"]