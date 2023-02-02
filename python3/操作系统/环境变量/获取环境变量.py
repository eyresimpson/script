import os

# Get all system environment variables
print("System Environment Variables:")
for key in os.environ:
    print(key, ":", os.environ[key])

print("\nUser Environment Variables:")
# Get all user environment variables
for key in os.environ:
    if key.startswith("USER"):
        print(key, ":", os.environ[key])
