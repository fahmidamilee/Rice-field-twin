
import paho.mqtt.client as mqtt
import json
import random
import time

broker = "test.mosquitto.org"
topic = "ricefield/iot"

client = mqtt.Client()
client.connect(broker, 1883, 60)

def generate_data():
    return {
        "temp": round(random.uniform(25, 38), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "soil_moisture": round(random.uniform(20, 60), 2),
        "ph": round(random.uniform(5.5, 7.5), 2)
    }

while True:
    data = generate_data()
    payload = json.dumps(data)
    client.publish(topic, payload)
    print("Published:", payload)
    time.sleep(5)
