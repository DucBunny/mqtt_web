import paho.mqtt.client as mqtt

BROKER = "192.168.1.187"  # Địa chỉ IP của Mosquitto Broker
PORT = 1883
TOPIC = "test/topic"

def on_message(client, userdata, message):
    print(f"Received: {message.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

print("Waiting for messages...")
client.loop_forever()

