import datetime
from time import sleep

import paho.mqtt.client as mqtt

devc = mqtt.Client()
mqttc = mqtt.Client()
devc.connect("localhost", 1883, 60)
mqttc.connect("airq.pl", 1883, 60)

timestamp = datetime.datetime.now().timestamp()
MESSAGE = '''{
"eventType": "AirqMeasurement",
"timestamp": "${timestamp}",
"payload": {
"humidity": 1,
"temperature": 12.3,
"pm10": 24.4,
"pm25": 3.1,
"location": "test",
"stationId": "test"
}
}'''.replace('\n', '').replace('${timestamp}', str(int(timestamp)))

while True:
    # devc.publish("/airq/sensors", MESSAGE, qos=0, retain=False)
    mqttc.publish("/airq/sensors", MESSAGE, qos=0, retain=True)
    print("send...")
    sleep(10)
