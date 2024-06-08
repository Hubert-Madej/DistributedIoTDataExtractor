import os
import random
import time
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from utils.config import load_config

load_config()
load_dotenv()

# @TODO - Add device information to simulator.
# @TODO - Add device certificates and auth into to simulator.

host = os.getenv("BROKER_ADDRESS", "localhost")
port = os.getenv("BROKER_PORT", 1883)
topic = os.getenv("TOPIC", "iot-device")

def generate_mock_data():
  temperature = random.randint(20, 30)
  humidity = round(random.uniform(40, 60), 2)
  timestamp = int(time.time())
  
  data = {
    "temperature": temperature,
    "humidity": humidity,
    "timestamp": timestamp
  }
  
  return data

  
def main():
  # Setup MQTT Client
  client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
  
  try:
    client.connect(host, port, 60)
  except Exception as e:
    print(f"Error: {e}")
    return

  batch = 10
  while batch > 0:
    # Generate Mock Data
    data = generate_mock_data()
    
    # Publish Data as IoT Device
    client.publish(topic, str(data))
    
    print(f"Published: {data}")
    
    batch -= 1
    time.sleep(5)
  
  client.disconnect()
  
if __name__ == "__main__":
  main()