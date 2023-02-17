import paho.mqtt.client as mqtt
# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connection returned result: " + str(rc))
  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  client.subscribe("ece180d/test", qos=1)
  client.subscribe("ece180a/test", qos=1)
# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
  if rc != 0:
    print('Unexpected Disconnect')
  else:
    print('Expected Disconnect')
# The default message callback.
# (you can create separate callbacks per subscribed topic)
def on_message(client, userdata, message):
  t = (str(message.payload)).split(" ")
  print('Received message: "' + str(message.payload) + '" on topic "' + message.topic + '" with QoS ' + str(message.qos))

  # checking if we push forward, IMU must be flat against hand
  if (len(t) > 2):
    s = t[0][2:].split("-")
    if (len(s[0]) > 0 and int(s[0].split(".")[0]) > 500):
      print("PUSH FORWARD")
  # checking if we push down, IMU must be flat against hand
    a = t[1].split("-")
    if (len(a[0]) > 0 and int(a[0].split(".")[0]) > 1000):
      print("PUSH DOWN")
  # checking if we wave to the left, IMU must be flat against hand
    b = t[1].split("'")[0].split("-")
    if (len(b[0]) > 0 and int(b[0].split(".")[0]) > 150):
      print("LEFT WAVE")




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
client.connect_async('mqtt.eclipseprojects.io')
# client.connect("test.mosquitto.org", 1883, 60)
# client.connect("mqtt.eclipse.org")
# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()
# client.loop_forever()
while True:  # perhaps add a stopping condition using some break or something.
  pass  # do your non-blocked other stuff here, like receive IMU data or something.
# use subscribe() to subscribe to a topic and receive messages.
# use publish() to publish messages to the broker.
# use disconnect() to disconnect from the broker.
client.loop_stop()
client.disconnect()