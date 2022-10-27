import requests
import time
import os.path
from datetime import datetime

timestamp = time.time()
print(f"Current timestamp: {timestamp} / {datetime.fromtimestamp(timestamp)}")
r = requests.get("https://www.google.com/")


def save_file(result):
    with open("result.txt", "w") as file:
        file.write(result.text)
        print("File was saved")


if os.path.exists("result.txt"):
    print("File already exists. Do you want to overwrite it?")
    confirmation = input("Do you want to overwrite it ? [y/n]")
    if confirmation.lower() in ["y", "yes"]:
        save_file(r)
else:
    save_file(r)


