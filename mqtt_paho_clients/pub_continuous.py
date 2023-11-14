import paho.mqtt.client as mqtt
import random
import time

def getMsg():
    d = random.randrange(20, 36)
    msg = str(d)                
    return msg                

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

mqttc.connect("localhost")
mqttc.loop_start()

try:
    while True:
        t = getMsg()
        print("temp", t)
        
        infot = mqttc.publish("room1/temp", t)
        infot.wait_for_publish()
        
        time.sleep(1)
except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()

