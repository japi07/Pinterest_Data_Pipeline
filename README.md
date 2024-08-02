# Kafka Data Streaming Project

## Table of Contents
1. [Project Description](#project-description)
2. [Installation Instructions](#installation-instructions)
3. [Usage Instructions](#usage-instructions)
4. [File Structure](#file-structure)
5. [License](#license)

## Project Description

This project involves setting up a data streaming pipeline using AWS Managed Streaming for Apache Kafka (MSK), Python, and Amazon S3. The goal is to stream data from three different tables (`pinterest_data`, `geolocation_data`, and `user_data`) to Kafka topics and store the streamed data in an S3 bucket.

### Aim of the Project

- To learn and implement data streaming using Kafka.
- To use AWS MSK for managing Kafka clusters.
- To stream data to Kafka topics and verify its consumption.
- To store streamed data in Amazon S3 for further processing and analysis.

### What You Learned

- Setting up and configuring Kafka and AWS MSK.
- Using Python for data extraction and posting to Kafka topics.
- Consuming data from Kafka topics.
- Storing streamed data in Amazon S3.

## Installation Instructions

### Prerequisites

- AWS account with necessary permissions for MSK and S3.
- Python 3.x installed.
- Kafka installed (preferably version 2.8.1).
- Necessary Python packages: `requests`, `boto3`, `sqlalchemy`, `pymysql`, `PyYAML`.

### Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/kafka-data-streaming-project.git
    cd kafka-data-streaming-project
    ```

2. **Install Required Python Packages:**

    ```bash
    pip install requests boto3 sqlalchemy pymysql PyYAML
    ```

3. **Set Up AWS MSK:**

    - Follow AWS documentation to set up an MSK cluster.
    - Note down the Kafka broker endpoints.

4. **Set Up S3 Bucket:**

    - Create an S3 bucket to store streamed data.

5. **Create `db_creds.yaml` File:**

    ```yaml
    HOST: <your-db-host>
    USER: <your-db-username>
    PASSWORD: <your-db-password>
    DATABASE: <your-database-name>
    PORT: <your-db-port>
    ```

## Usage Instructions

1. **Running the Python Script:**

    ```bash
    python user_posting_emulation.py
    ```

    This script will randomly select rows from the three tables and post the data to the configured API endpoint, which forwards the data to Kafka topics.

2. **Consuming Data from Kafka Topics:**

    Navigate to your Kafka installation directory and run the following command:

    ```bash
    ./bin/kafka-console-consumer.sh --bootstrap-server <kafka-broker-endpoints> --topic <your-topic> --from-beginning
    ```

    Replace `<kafka-broker-endpoints>` and `<your-topic>` with appropriate values.

3. **Verifying Data in S3:**

    Use the AWS Management Console or AWS CLI to check if the data is stored in the S3 bucket:

    ```bash
    aws s3 ls s3://<your_s3_bucket>/topics/
    ```


