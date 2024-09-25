import os
import requests
from datetime import datetime

# Function to manually log messages to the log file
def simple_log(message):
    with open("log.txt", "a") as log_file:
        # log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # log_file.write(f"{log_time} - {message}\n")
        log_file.write(f" {message}\n")

# Handling secret token
try:
    SOME_SECRET = os.environ["SOME_SECRET"]
    simple_log(f"The token is {SOME_SECRET}")
except KeyError:
    # SOME_SECRET = "Token not available!"
    simple_log("Token not available!")

# Main application logic
if __name__ == "__main__":
    # simple_log(f"Token value: {SOME_SECRET}")

    try:
        r = requests.get('https://www.arbeitnow.com/api/job-board-api')
        if r.status_code == 200:
            api_content = r.json()
            jobs = api_content["data"]
            for job in jobs:
                simple_log(f"Company {job["company_name"]}\n position :  {job["title"]}")
        else:
            simple_log(f"Failed to retrieve weather data. Status code: {r.status_code}")
    except Exception as e:
        simple_log(f"An error occurred: {str(e)}")
