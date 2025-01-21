import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?")
}

response = requests.post(pixel_creation_endpoint, json=pixel_config, headers=headers)

update_pixel_endpoint = f"{pixel_creation_endpoint}/20250117"

pixel_update = {
    "quantity": "20",
}

response = requests.put(update_pixel_endpoint, json=pixel_update, headers=headers)

delete_pixel_endpoint =  f"{pixel_creation_endpoint}/20250117"

response = requests.delete(delete_pixel_endpoint, headers=headers)
print(response.text)
