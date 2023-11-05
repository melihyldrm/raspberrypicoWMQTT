import network
from umqtt.simple import MQTTClient
import time

mqtt_server = 'broker.hivemq.com'
client_id = 'raspi_pico_w'
topic_pub = b'melihy'

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("yourWIFIAddress", "yourWIFIParola")
while not wlan.isconnected():
    pass

# Initialize the MQTT client
client = MQTTClient(client_id, mqtt_server, keepalive=3600)
client.connect()
print('Connected to %s MQTT Broker' % (mqtt_server))

while True:
    # Read sensor data or perform desired actions
    # ...
    
    # Create the MQTT message
    topic_msg = "message taken correctly!"
    # Publish the MQTT message
    client.publish(topic_pub, topic_msg)
    
    # Delay between messages
    time.sleep(3)

