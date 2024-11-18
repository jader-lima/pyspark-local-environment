# setup.py
from setuptools import setup, find_packages

setup(
    name="lib_custom_python",
    version="0.1.0",
    package_dir={'': 'src'},
    packages=find_packages('src', include=[
            '*'
        ], exclude=[
            ''
        ]),
        install_requires=[
            'pyspark==3.5.0','delta-spark==3.2.0','pytest'
        ],

    # metadata
    author="Seu Nome",
    author_email="seuemail@example.com",
    description="short lib descripton",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_user/your_library", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8.4",  # python version
)
