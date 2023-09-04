import re
with open("file.html","r") as f:
	contents = f.read()
	pattern = r'\d{21}'
	matches = re.findall(pattern, contents)
	print(matches)