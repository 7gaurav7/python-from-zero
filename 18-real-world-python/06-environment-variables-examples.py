"""
18 - Real-World Python: Environment Variables
Runnable examples matching the lesson.
Outputs depend on which environment variables are set in your terminal --
running this with no variables set is expected and shows the fallback
defaults.
"""
import os

# Example 1: reading an environment variable with a default
debug_mode = os.environ.get("DEBUG", "False")
print(f"Debug mode: {debug_mode}")

# Example 3: using an environment variable to choose behavior
environment = os.environ.get("APP_ENV", "development")
if environment == "production":
    print("Running with production settings.")
else:
    print("Running with development settings.")

# Example 4 requires `pip install python-dotenv` and a .env file, so it's
# shown here only as a comment -- see the lesson file for the full example.
# from dotenv import load_dotenv
# load_dotenv()
# api_key = os.environ.get("SECRET_API_KEY", "not set")
# print(f"API key loaded: {api_key != 'not set'}")
