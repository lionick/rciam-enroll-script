import csv
import json
import requests

# Define your API base URL
VO_API_BASE_URL = "https://your-api-base-url.com"

# Function to make the POST request for each epuid
def make_request(epuid):
    # Load JSON data from add.json template
    with open("add.json") as f:
        data = json.load(f)
    
    # Replace placeholder with epuid from CSV file
    data["CoPersonRoles"][0]["Person"]["Identifier"]["Id"] = epuid
    
    # Make POST request
    response = requests.post(
        f"{VO_API_BASE_URL}.json",
        auth=("example-client", "veryverysecret"),
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