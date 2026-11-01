import sqlite3, numpy, flask
import paho.mqtt.client as mqtt

got = []
def on_message(c, u, msg):
    got.append(msg.payload.decode())

# paho-mqtt 2.x requires the callback API version argument
sub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
sub.on_message = on_message
sub.connect("localhost", 1883)
sub.subscribe("check/topic")
sub.loop_start()

pub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
pub.connect("localhost", 1883)
pub.loop_start()
import time; time.sleep(0.5)
pub.publish("check/topic", "ok")
time.sleep(0.5)

print("MQTT:", got)            # expect ['ok']
print("SQLite:", sqlite3.sqlite_version)
print("NumPy:", numpy.__version__)
print("Flask:", flask.__version__)
