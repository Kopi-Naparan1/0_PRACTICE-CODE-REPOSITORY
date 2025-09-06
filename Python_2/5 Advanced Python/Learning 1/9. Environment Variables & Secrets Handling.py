import os

print("All environment variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

print("\nGet a specific one:")
print("USERNAME:", os.getenv("USERNAME"))  # or "USER" on Linux/Mac


print("MY_SECRET:", os.getenv("MY_SECRET"))
