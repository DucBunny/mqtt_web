import paho.mqtt.client as mqtt
import time

BROKER = "127.0.0.1"  # Local MQTT broker
PORT = 1883
TOPIC = "test/topic"

client = mqtt.Client()

client.connect(BROKER, PORT, 60)

while True:
    message = f"Hello Subscriber! Time: {time.time()}"
    print(f"Publishing: {message}")
    client.publish(TOPIC, message)
    time.sleep(1)  # Publish message every second