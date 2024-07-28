
##Pinterest_Data_Pipeline

Table of Contents

Description
Installation
Usage
File Structure
License
Description

This project demonstrates how to configure a Kafka client to use AWS IAM for authentication. The aim is to securely connect to an AWS MSK cluster using IAM roles. Through this project, we learn how to configure Kafka clients, manage topics, and utilize AWS IAM for secure authentication.

What I Learned
Configuring Kafka clients for AWS IAM authentication.
Managing Kafka topics via command line.
Secure communication using SASL_SSL.
Installation

To set up the project, follow these steps:

Clone the repository:
sh
Copy code
git clone <repository-url>
cd <repository-directory>
Navigate to the Kafka installation folder:
sh
Copy code
cd /path/to/kafka
Create and edit the client properties file:
sh
Copy code
nano bin/client.properties
Add the following content:

properties
Copy code
security.protocol = SASL_SSL
sasl.mechanism = AWS_MSK_IAM
sasl.jaas.config = software.amazon.msk.auth.iam.IAMLoginModule required awsRoleArn="arn:aws:iam::584739742957:role/1244224ff301-ec2-access-role";
sasl.client.callback.handler.class = software.amazon.msk.auth.iam.IAMClientCallbackHandler
Usage

Create Kafka topics:
sh
Copy code
./kafka-topics.sh --bootstrap-server b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098 --create --topic 1244224ff301.pin --command-config client.properties
./kafka-topics.sh --bootstrap-server b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098 --create --topic 1244224ff301.geo --command-config client.properties
./kafka-topics.sh --bootstrap-server b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098 --create --topic 1244224ff301.user --command-config client.properties
List Kafka topics:
sh
Copy code
./kafka-topics.sh --bootstrap-server b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098 --list --command-config client.properties
