# setup.py
from setuptools import setup, find_packages

setup(
    name="lib_confluent_kafka_python",
    version="0.1.0",
    package_dir={'': 'src'},
    packages=find_packages('src', include=[
            'lib_confluent_kafka_python*'
        ], exclude=[
            ''
        ]),
        install_requires=[
            'confluent-kafka==2.3.0'
        ],

    # Metadata
    author="jaderlima",
    author_email="you-email@example.com",
    description="custom python library based on confluent-kafka library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://https://github.com/jader-lima/pyspark-local-environment/tree/python-kafka-consumer-producer-classes-post1", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8.4",  # Python min version
)
