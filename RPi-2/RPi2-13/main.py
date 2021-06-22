import paho.mqtt.client as mqtt  # import the client1
import time


############
def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)


########################################

broker_address = "broker.mqttdashboard.com"
# broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("my_id_wesley_vercoutere")  # create new instance
client.on_message = on_message  # attach function to callback

print("connecting to broker")
client.connect(broker_address)  # connect to broker

client.loop_start()  # start the loop

print("Subscribing to topic", "cvofocus/wimverlinden")
client.subscribe("cvofocus/wimverlinden")

print("Publishing message to topic", "cvofocus/wimverlinden")
client.publish("cvofocus/wimverlinden", "??????")

try:
    while True:
        pass

except:
    client.loop_stop()
    print("session finished")
