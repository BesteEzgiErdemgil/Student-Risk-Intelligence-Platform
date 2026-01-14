
import os
from dotenv import load_dotenv

# Path to the .env file
env_path = '.env/.env'

print(f"Attempting to load .env from: {os.path.abspath(env_path)}")

if not os.path.exists(env_path):
    print(f"Error: File not found at {env_path}")
else:
    # Load dotenv
    loaded = load_dotenv(dotenv_path=env_path)
    if loaded:
        print("Success: .env file loaded.")
        # Print all keys loaded (don't print values for security if they were real secrets, but here we just want to see it works)
        # For verification, we can just say it loaded.
        # Check if there are any variables in it.
        with open(env_path, 'r') as f:
            content = f.read()
            if not content.strip():
                print("Warning: .env file is empty.")
            else:
                print("File has content.")
                # print("Dumping content for debugging:")
                # print(content)
    else:
        print("Warning: load_dotenv returned False (maybe file is empty or malformed).")
