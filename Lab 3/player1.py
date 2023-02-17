import paho.mqtt.client as mqtt
import numpy as np
import time


# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    client.subscribe("gamep1/test", qos=1)
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
# client.subscribe("ece180d/test")
# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")
# The default message callback.
# (won’t be used if only publishing, but can still exist)
def on_message(client, userdata, message):
    #print("Received message: " + str(message.payload) + " on topic " + message.topic + " with QoS " + str(message.qos))
    print(str(message.payload))
    move = int(input("Choose Rock: 1, Paper: 2, or Scissors: 3 \n"))
    client.publish("gamep2/test", move, qos=1)
# 1. create a client instance.
client = mqtt.Client()
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
# 2. connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async("mqtt.eclipseprojects.io")
# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()
# 4. use subscribe() to subscribe to a topic and receive messages.
# 5. use publish() to publish messages to the broker.
# payload must be a string, bytearray, int, float or None.
print("Publishing...")
while True: # perhaps add a stopping condition using some break or something.
    pass
# 6. use disconnect() to disconnect from the broker.
client.loop_stop()
client.disconnect()