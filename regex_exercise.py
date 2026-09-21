import re

# TASK 1
log_lines = [
    "2024-01-15 10:02:11 INFO Server started on port 8080",
    "2024-01-15 10:03:47 ERROR Failed to connect to database",
    "2024-01-16 08:15:00 WARNING Disk usage at 85%",
    "2024-01-16 14:22:39 ERROR Timeout while fetching https://example.com/api",
    "2024-01-17 09:00:05 INFO User admin logged in from 192.168.1.10",
    "2024-01-17 11:41:18 DEBUG Cache cleared successfully",
    "2024-01-18 03:12:56 ERROR Connection refused from 192.168.1.55",
    "2024-01-18 23:59:02 INFO Backup completed in 42s",
]

# 1. Find all lines logged on 2024-01-16

for line in log_lines:
    if re.search(r"^2024-01-16", line): # or re.match
        print(line)


# 2. Find all lines that are an ERROR or a WARNING

for line in log_lines:
    if re.search(r"ERROR|WARNING", line):   #altgr + w → |
        print(line)

# 3. Find all IPv4 addresses (four groups of 1-3 digits separated by dots) that appear anywhere
# in the log — only 2 of the 8 lines contain one.

for line in log_lines:
    match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
    if match:
        print(match.group())

# 4. Find all lines ending in a number of seconds, e.g. ...in 42s.

for line in log_lines:
    if re.search(r"\d+s$", line):
        print(line)

# 5. Find all lines that mention a URL (starts with http:// or https://).

for line in log_lines:
    if re.search(r"https?://", line):
        print(line)

# 6. Check whether a single line, e.g. log_lines[0], matches the full expected
# format YYYY-MM-DD HH:MM:SS LEVEL message from start to end.

pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Z]+ .+$"
print(bool(re.fullmatch(pattern, log_lines[0])))

# TASK 2

class SequencingRead:
    def __init__(self, line):