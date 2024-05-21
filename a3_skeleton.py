import asyncio
import time
import json

from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message

# Define the connection string
CONNECTION_STRING = ""

async def connect():
    device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    await device_client.connect()
    print('connected')
    return device_client

async def send_data(device_client, points):
    for count, point in enumerate(points):
        data = json.dumps({"lat": point[1], "lng": point[0], "count": count})
        message = Message(data)
        await device_client.send_message(message)
        print(f"Message {count} successfully sent: {data}")
        await asyncio.sleep(0.5)  # delay before sending the next point

def load_route_data(file_path):
    with open(file_path, 'r') as file:
        route_data = json.load(file)
    return route_data["features"][0]["geometry"]["coordinates"]

def main():
    device_client = asyncio.run(connect())

    # Load coordinates from the route file
    coordinates = load_route_data('route1.json')

    asyncio.run(send_data(device_client, coordinates))

    # finally, shut down the client
    asyncio.run(device_client.shutdown())

if __name__ == "__main__":
    main()
