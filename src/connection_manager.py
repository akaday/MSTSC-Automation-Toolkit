# Python script to manage remote connections
import os

def connect_to_server(server_address):
    os.system(f'mstsc /v:{server_address}')

def disconnect_from_server():
    os.system('tsdiscon')

# Add more functions as needed
