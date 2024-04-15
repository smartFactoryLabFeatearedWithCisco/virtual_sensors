import socketio
import time
import os
import json


# Create a Socket.IO client
sio = socketio.Client()

# Define the event handler for the "connect" event
@sio.event
def connect():
    print("I'm connected!")
    sio.emit('chat message', 'Client1 connected')

# Define the event handler for the "chat message" event
@sio.on('chat message')
def message(data):
    print(data)

@sio.on('sizak')
def message():
    sizak = True
    # Iterate over each JSON file
    for json_file in json_files:
        time.sleep(1)
        # Construct the full path to the JSON file
        json_path = os.path.join(json_dir, json_file)
    
        # Open the JSON file and load the data
        with open(json_path, 'r') as f:
            data = json.load(f)
        data = json.dumps(data)

        # Now you can use the data from the JSON file
        print(f"Loaded Advs data from " + str(data))

        sio.emit('sensor Data', data)

@sio.on('emergency stop')
def message():
    print("emergency stopping!")


# Define the event handler for the "disconnect" event
@sio.event
def disconnect():
    print("I'm disconnected!")
    sio.connect('http://10.225.5.5:3000', transports=['websocket'])

# Specify the directory where the JSON files are stored
json_dir = "meltingM/Advs"

# Get a list of all JSON files in the directory
json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

# Sort the list of files
json_files.sort()

# Connect to the server
sio.connect('http://10.225.5.5:3000', transports=['websocket'])

sizak = False

while True:
    if sizak:
        

    else:
        time.sleep(1)
        temp_json_path = os.path.join(json_dir, "0.json")
        # Open the JSON file and load the data
        with open(temp_json_path, 'r') as f:
            data = json.load(f)
        data = json.dumps(data)

        # Now you can use the data from the JSON file
        print(f"Loaded Temps data from " + str(data))

        sio.emit('sensor Data', data)
    
    
    
    

'''
for i in range(100):
    time.sleep(0.1)
    # Send a message to the server
    sio.emit('chat message', 'Hello from Python Client!')
    print(i)
'''
# Send a message to the server
sio.emit('chat message', 'Hello from Python Client!')

# Disconnect from the server
sio.disconnect()
