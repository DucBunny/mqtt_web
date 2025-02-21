import paho.mqtt.client as mqtt
import time

BROKER = "192.168.1.187"  # IP của thiết bị chạy Mosquitto
PORT = 1883
TOPIC = "test/topic"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

while True:
    message = f"Hello from {BROKER} at {time.time()}"
    print(f"Publishing: {message}")
    client.publish(TOPIC, message)
    time.sleep(2)
