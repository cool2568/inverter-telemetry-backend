import json
import asyncio
import paho.mqtt.client as mqtt
from app.core.database import AsyncSessionLocal
from app.services.telemetry_service import TelemetryService

MQTT_BROKER="13.201.114.43"
MQTT_PORT=1883
MQTT_USERNAME='rdinverter'
MQTT_PASSWORD='rdinverter'

MQTT_TOPIC="inverter/+/data"


def on_message(client,userdata,msg):
    payload=json.loads(msg.payload.decode())
    device_uid=msg.topic.split("/")[1]

    async def process():
        async with AsyncSessionLocal() as db:
            await TelemetryService.ingest_from_mqtt(
                db=db,
                device_uid=device_uid,
                payload=payload
            )
    asyncio.run(process())

client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.connect(MQTT_BROKER, MQTT_PORT)

client.subscribe(MQTT_TOPIC)
client.on_message = on_message

print("✅ MQTT Telemetry Worker Running...")
client.loop_forever()   