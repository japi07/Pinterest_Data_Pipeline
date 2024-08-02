import requests
from time import sleep
import random
from multiprocessing import Process
import json
import sqlalchemy
from sqlalchemy import text
import yaml

random.seed(100)

class AWSDBConnector:

    def __init__(self):
        # Load database credentials from the yaml file
        with open('db_creds.yaml', 'r') as file:
            creds = yaml.safe_load(file)
            self.HOST = creds['HOST']
            self.USER = creds['USER']
            self.PASSWORD = creds['PASSWORD']
            self.DATABASE = creds['DATABASE']
            self.PORT = creds['PORT']
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()

# Kafka REST Proxy URL
KAFKA_REST_PROXY_URL = 'https://fi7y6mrwcg.execute-api.us-east-1.amazonaws.com/1244224ff301'  # Update with your actual URL

# Kafka topics
TOPICS = {
    'pinterest_data': 'pinterest_topic',
    'geolocation_data': 'geolocation_topic',
    'user_data': 'user_topic'
}

def send_data_to_kafka(topic, data):
    url = f'{KAFKA_REST_PROXY_URL}/topics/{topic}'
    headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
    payload = {'records': [{'value': data}]}

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print(f'Successfully sent data to topic {topic}')
    else:
        print(f'Failed to send data to topic {topic}: {response.content}')

def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            # Fetch data from the database
            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)

            # Print data (for debugging)
            print(pin_result)
            print(geo_result)
            print(user_result)

            # Send data to Kafka topics
            send_data_to_kafka(TOPICS['pinterest_data'], pin_result)
            send_data_to_kafka(TOPICS['geolocation_data'], geo_result)
            send_data_to_kafka(TOPICS['user_data'], user_result)

if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')