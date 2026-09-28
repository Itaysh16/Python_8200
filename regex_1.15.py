import re

mixed_string = "My name is Itay. I am 16 year-old and I am 1.63 meters"
numbers = re.findall(r'\d+\.\d+|\d+', mixed_string)
print(f"Numbers found: {numbers}")

capita_words = re.findall(r"\b[A-Z]\w*\b", mixed_string)
print("The capital words are: ", capita_words)

import re
from collections import Counter

# ==========================================
# תרגיל 1: חימום
# ==========================================
mixed_string = "My name is Itay. I am 16 year-old and I am 1.63 meters"

numbers = re.findall(r"\d+\.?\d*", mixed_string)
print("Numbers found:", numbers)

capital_words = re.findall(r"\b[A-Z]\w*\b", mixed_string)
print("The capital words are:", capital_words)


# ==========================================
# תרגיל 2: ניתוח קובץ לוג של שרת
# ==========================================
def analyze_server_log(log_file_path):
    log_pattern = (
        r"(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?\b(?P<status>\d{3})\b"
    )

    ip_counter = Counter()
    error_count = 0
    total_requests = 0

    try:
        with open(log_file_path, "r", encoding="utf-8") as f:
            log_data = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' was not found.")
        return

    for match in re.finditer(log_pattern, log_data):
        total_requests += 1

        ip = match.group("ip")
        status = match.group("status")

        ip_counter[ip] += 1

        if status.startswith(("4", "5")):
            error_count += 1

    print("\n================ LOG ANALYSIS REPORT ================")
    print(f"Total Log Entries Processed   : {total_requests}")
    print(f"Total Unique IP Addresses     : {len(ip_counter)}")
    print(f"Total Error Requests (4xx/5xx): {error_count}")
    print("\nRequests per IP Address:")
    print("-" * 35)
    for ip, count in ip_counter.items():
        print(f"  {ip:<18} : {count} requests")
    print("=====================================================")


if __name__ == "__main__":
    analyze_server_log("server.log")