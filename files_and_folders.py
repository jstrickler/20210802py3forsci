import os
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "mary.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print("file_path: {}\n".format(file_path))

print(os.path.exists(file_path))
print(os.path.exists("wombats.txt"))
print()

print("os.path.dirname(file_path): {}\n".format(os.path.dirname(file_path)))
print("os.path.basename(file_path): {}\n".format(os.path.basename(file_path)))
print("os.path.abspath(file_path): {}\n".format(os.path.abspath(file_path)))

print("os.path.split(file_path): {}\n".format(os.path.split(file_path)))

file_size = os.path.getsize(file_path)
raw_timestamp = os.path.getmtime(file_path)
timestamp = datetime.fromtimestamp(raw_timestamp)
print("file_size: {}\n".format(file_size))
print("raw_timestamp: {}\n".format(raw_timestamp))
print("timestamp: {}\n".format(timestamp))










