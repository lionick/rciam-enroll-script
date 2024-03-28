## Setting Up Environment for Running the Script

### 1. Clone the Repository
Clone the repository containing your Python script and necessary files.

```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Create a Virtual Environment
Create a virtual environment to isolate dependencies.

```bash
# For Unix/Linux/MacOS
python3 -m venv env
```

### 3. Activate the Virtual Environment
Activate the virtual environment.

```bash
# For Unix/Linux/MacOS
source env/bin/activate
```

### 4. Install Required Packages
Install the required packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5. Replace Placeholder Values
Replace the following placeholder values in the Python script (`enroll.py`) with your actual values:

- `https://your-api-base-url.com`: Replace this with the base URL of your API.
- `example-client`: Replace with your API client username.
- `veryverysecret`: Replace with your API client password.

### 6. Provide JSON Template
Ensure that you have a JSON template file named `add.json` in the same directory as the script. This JSON file should contain the template for the POST request payload.

### 7. Prepare CSV File
Prepare a CSV file named `epuids.csv` containing the epuids in the specified format (one epuid per row).

## Running the Script
Once you have completed the setup, you can run the script using the following command:

```bash
python enroll.py
```

The script will read epuids from the CSV file, make a POST request for each epuid using the provided JSON template, and print the response for each request.


