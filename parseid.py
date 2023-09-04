import re
import argparse

parser = argparse.ArgumentParser(description="Find 21-character strings of numbers in a file")

parser.add_argument("-f", "--file", required=True, help="File name to extract ID from")

args = parser.parse_args()

try:
    with open(args.file, "r") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Error: File '{args.file}' not found.")
    exit(1)

pattern = r'\d{21}'
matches = re.findall(pattern, contents)
print(f"Found: {matches[0]}")
