"""
18 - Real-World Python: Configuration Basics
Runnable examples matching the lesson.
Running this script creates 'config.json' in this folder.
"""
import json

# Example 2: loading configuration from JSON
with open("config.json", "w") as file:
    json.dump({"app_name": "Contact Book", "max_results": 50}, file)

with open("config.json", "r") as file:
    config = json.load(file)

print(config["app_name"])
print(config["max_results"])
# Expected output:
# Contact Book
# 50

# Example 3: providing sensible defaults if a setting is missing
settings = {"app_name": "Contact Book"}  # "max_results" was never set
max_results = settings.get("max_results", 100)
print(max_results)
# Expected output: 100

# Example 4: different configuration per environment
import os  # noqa: E402

ENVIRONMENT = os.environ.get("APP_ENV", "development")

if ENVIRONMENT == "production":
    DATA_FILE = "prod_contacts.txt"
    DEBUG = False
else:
    DATA_FILE = "dev_contacts.txt"
    DEBUG = True

print(f"Running in {ENVIRONMENT} mode, using {DATA_FILE}")
