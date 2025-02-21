import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"
PORT = 1883
TOPIC = "test/topic"

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

print("Waiting for messages...")
client.loop_forever()
