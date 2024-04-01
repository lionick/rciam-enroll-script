import csv
import json
import requests

# Load configuration from config.json
with open("config.json") as f:
    config = json.load(f)

# Define API base URL and authentication credentials
VO_API_BASE_URL = config["api_base_url"]
USERNAME = config["username"]
PASSWORD = config["password"]
COU_NAME = config["cou_name"]
VALID_FROM = config["start_date"]
VALID_THROUGH = config["end_date"]

# Function to make the POST request for each epuid
def make_request(epuid):
    # Load JSON data from add.json template
    with open("add.json") as f:
        data = json.load(f)
    
    # Replace placeholder with epuid from CSV file
    data["CoPersonRoles"][0]["Person"]["Identifier"]["Id"] = epuid
    data["CoPersonRoles"][0]["Cou"]["Name"] = COU_NAME
    data["CoPersonRoles"][0]["ValidFrom"] = VALID_FROM
    data["CoPersonRoles"][0]["ValidThrough"] = VALID_THROUGH
    
    # Make POST request
    response = requests.post(
        f"{VO_API_BASE_URL}.json",
        auth=(USERNAME, PASSWORD),
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    # Print response
    print(f"Response for epuid {epuid}: {response.status_code}")
    print(response.text)

# Read epuids from CSV file and make requests
with open("epuids.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        epuid = row[0].strip()  # Assuming epuid is in the first column, strip any leading/trailing spaces
        make_request(epuid)