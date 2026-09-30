import re
from collections import Counter

audit_data = """
2026-09-30 10:15:00 [USER: alex_k] [EMAIL: alex@company.com] ACTION: LOGIN_SUCCESS
2026-09-30 10:15:22 [USER: bot_test] [EMAIL: test@hacker.org] ACTION: LOGIN_FAILED
2026-09-30 10:16:05 [USER: alex_k] [EMAIL: alex@company.com] ACTION: FILE_DELETE
2026-09-30 10:17:10 [USER: bot_test] [EMAIL: test@hacker.org] ACTION: LOGIN_FAILED
2026-09-30 10:18:00 [USER: sara_dev] [EMAIL: sara@company.com] ACTION: LOGIN_SUCCESS
2026-09-30 10:19:45 [USER: bot_test] [EMAIL: test@hacker.org] ACTION: LOGIN_FAILED
"""

pattern = r'\[USER:\s*(?P<user>\w+)\]\s+\[EMAIL:\s*(?P<email>[\w.-]+@[\w.-]+)\]\s+ACTION:\s*(?P<action>\w+)'
failed_attempts = Counter()
user_emails ={}

for match in re.finditer(pattern, audit_data):
    user = match.group("user")
    email = match.group("email")
    action = match.group("action")
    user_emails[user] = email
    if action == "LOGIN_FAILED":
        failed_attempts[user] += 1

for user, count in failed_attempts.items(): 
    if count > 2:
        print(f"[ALERT] Suspicious activity detected for user: {user} (email: {user_emails[user]}) - {count} failed logins!")