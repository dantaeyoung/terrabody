import json
import sys
import asyncio
import aiohttp
from common.pubsub import Pubsub


ps = Pubsub()

base_ip = "192.168.0.165"  # Replace with your actual base IP address

async def control_light(light_number, data):
    base_url = f"http://{base_ip}/api/V826YDVHybl2XnSJrFrYEVcRcL0zcVPkQH1YKTSP"
    light_url = f"{base_url}/lights/{light_number}/state"

    async with aiohttp.ClientSession() as session:
        async with session.put(light_url, json=data) as response:
            if response.status == 200:
                print(f"Successfully updated light {light_number}")
            else:
                print(f"Failed to update light {light_number}. Status code: {response.status}")

json_data = {"1": {"xy": [0.675, 0.322], "on": "true", "bri": 200},
"2": {"xy": [0.367, 0.358], "on": "true", "bri": 200},
"3": {"xy": [0.190, 0.099], "on": "true", "bri": 200},
"6": {"xy": [0.453, 0.454], "on": "true", "bri": 200},
"7": {"xy": [0.555, 0.297], "on": "true", "bri": 200},
"8": {"xy": [0.408, 0.517], "on": "true", "bri": 200}}

async def main():
    try:
        # Read JSON input from stdin
        #input_str = sys.stdin.read()

        # Parse the JSON string into a Python object
        #json_data = json.loads(input_str)

        for light_number, data in json_data.items():
            await control_light(light_number, data)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

#asyncio.run(main())


while True:
    message = ps.recv_string()
    print(message)
    

    if "openai::" in message and "hue::" in message:
        print("HUE TIME")
        print(message.split("openai::")[1])
        #a.play()
        #a.close()


