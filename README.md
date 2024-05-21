# IoT Integration with Azure Cloud
## Prerequisite
Before starting this assignment, ensure you have a Microsoft Azure account with free $100 student credit. If you do not have an Azure account yet, follow these steps:

- Sign up for the GitHub Student Developer Pack using your university email address.
- Sign up for Azure through the GitHub Student Developer Pack to claim your free $100 credit.

## Task Instructions
Here is a brief summary of the steps involved:

### Steps in Brief
- Azure: Create an IoT hub
- Azure: Provision an IoT device
- Local: Install Python package azure-iot-device via pip
- Local: Test sending a single message to the hub
- Azure: Create a storage account
- Azure: Add a storage container in this account
- Azure: Create a stream analytics job
- Azure: Configure job’s inputs and outputs
- Azure: Write the job’s transformation query
- Both: Run the job, send IoT device data, and watch results in the storage container
**Warning**: Run the stream analytics job for the shortest time possible. Stop the job when not in use to avoid accumulating high costs.

## Tasks
### Task 1: Complete the Virtual IoT Device Python Code
Write Python code to sequentially send all latitude and longitude coordinates from a route file to the IoT hub.

## Sample Code
```
import time
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "Your IoT Hub Device Connection String"
ROUTE_FILE = "path/to/your/route_file.csv"

def read_route_file(file_path):
    with open(file_path, 'r') as file:
        coordinates = [line.strip().split(',') for line in file.readlines()]
    return coordinates

def send_message(client, lat, lng):
    message = Message(f'{{"latitude": {lat}, "longitude": {lng}}}')
    client.send_message(message)
    print(f"Message sent: {message}")

def main():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    coordinates = read_route_file(ROUTE_FILE)
    for lat, lng in coordinates:
        send_message(client, lat, lng)
        time.sleep(1)  # Delay to simulate real-time data sending

if __name__ == '__main__':
    main()
Task 2: Complete the Stream Analytics Query
Write the stream analytics query to compute the distance of each point to the destination (FAST campus).
```
## Sample Query
```
WITH GeoDistance AS (
    SELECT
        lat,
        lng,
        111.045 * DEGREES(ACOS(COS(RADIANS(@destination_lat)) * COS(RADIANS(lat)) * COS(RADIANS(lng) - RADIANS(@destination_lng)) + SIN(RADIANS(@destination_lat)) * SIN(RADIANS(lat)))) AS distance
    FROM
        input
)
SELECT
    lat,
    lng,
    distance
INTO
    output
FROM
    GeoDistance
Replace @destination_lat and @destination_lng with the latitude and longitude of the FAST campus.
```
## Conclusion
This assignment demonstrates how to integrate an IoT device with Azure Cloud, including sending data from a virtual device, processing it using stream analytics, and storing the results in an Azure storage container. Follow the steps and complete the tasks to achieve a successful integration.

## Contact
For any questions or further information, please feel free to reach out!
