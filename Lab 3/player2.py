import paho.mqtt.client as mqtt
import time


# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("gamep2/test", qos=1)
    client.publish("gamep1/test", 0, qos=1)

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")
# The default message callback.
# (you can create separate callbacks per subscribed topic)
def on_message(client, userdata, message):
    #print("Received message: " + str(message.payload) + " on topic " + message.topic + " with QoS " + str(message.qos))
    comp = int(message.payload)
    user = int(input("Choose Rock: 1, Paper: 2, or Scissors: 3 \n"))
    win = ""
    if (user == comp):
        win = ("Tie")
    if (user == 1):
        if (comp == 2):
            win = ("You Wins!")
        elif (comp == 3):
            win = ("Player 2 Wins!")
    elif (user == 2):
        if (comp == 3):
            win = ("You Wins!")
        elif (comp == 1):
            win = ("Player 2 Wins!")
    elif (user == 3):
        if (comp == 1):
            win = ("You Wins!")
        elif (comp == 2):
            win = ("Player 2 Wins!")
    else:
        print("Incorrect Input please try again.")
    client.publish("gamep1/test", win, qos=1)

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
# client.connect("test.mosquitto.org", 1883, 60)
# client.connect("mqtt.eclipse.org")
# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()
# client.loop_forever()
while True: # perhaps add a stopping condition using some break or something.
    pass # do your non-blocked other stuff here, like receive IMU data or something.
# use subscribe() to subscribe to a topic and receive messages.
# use publish() to publish messages to the broker.
# use disconnect() to disconnect from the broker.
client.loop_stop()
client.disconnect()