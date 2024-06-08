import paho.mqtt.client as mqtt
from kafka import KafkaProducer
import json
import socket

# Configuration
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'iot/sensor_data'

KAFKA_BROKER = 'kafka-broker:9092'
KAFKA_TOPIC = 'iot-data'

# Kafka Producer Setup
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda x: json.dumps(x).encode('utf-8'),
    api_version=(0, 10, 1),
    client_id=socket.gethostname()
)

# MQTT Callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print(f"Received message from MQTT: {msg.topic} {msg.payload.decode()}")
    
    # Processing the message (e.g., parsing JSON, transforming data)
    try:
        data = json.loads(msg.payload.decode())
        processed_data = process_data(data)
        print(f"Processed data: {processed_data}")
        
        # Send data to Kafka
        producer.send(KAFKA_TOPIC, value=processed_data)
        print("Data sent to Kafka")
    except Exception as e:
        print(f"Error processing message: {e}")

def process_data(data):
    data['processed'] = True
    return data

# MQTT Client Setup
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"Error: {e}")
    exit(1)

# Start MQTT loop
mqtt_client.loop_forever()