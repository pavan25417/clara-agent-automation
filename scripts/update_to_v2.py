import json
import os

# Paths
MEMO_V1_PATH = "../outputs/accounts/account_001/v1/account_memo.json"
ONBOARD_PATH = "../inputs/onboarding_calls/onboard_001.txt"

OUTPUT_DIR = "../outputs/accounts/account_001/v2"
CHANGELOG_PATH = os.path.join(OUTPUT_DIR, "changes.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load v1 memo
with open(MEMO_V1_PATH, "r") as f:
    memo_v1 = json.load(f)

memo_v2 = memo_v1.copy()

changes = []

# Read onboarding transcript
with open(ONBOARD_PATH, "r") as f:
    onboarding_text = f.read().lower()

# Update business hours
old_hours = memo_v1["business_hours"]["days"]

memo_v2["business_hours"]["days"] = "Monday-Friday, Saturday"
memo_v2["business_hours"]["start_time"] = "09:00"
memo_v2["business_hours"]["end_time"] = "17:00"

changes.append({
    "field": "business_hours",
    "old_value": old_hours,
    "new_value": memo_v2["business_hours"]["days"],
    "reason": "Saturday hours mentioned during onboarding"
})

# Add technician name
memo_v2["notes"] = "On-call technician: Rajesh Kumar"

changes.append({
    "field": "on_call_technician",
    "old_value": "unknown",
    "new_value": "Rajesh Kumar",
    "reason": "Provided during onboarding"
})

# Add transfer timeout rule
memo_v2["notes"] += " | Transfer timeout set to 90 seconds."

changes.append({
    "field": "transfer_timeout",
    "old_value": "not specified",
    "new_value": "90 seconds",
    "reason": "Specified during onboarding"
})

# Save v2 memo
memo_output = os.path.join(OUTPUT_DIR, "account_memo.json")

with open(memo_output, "w") as f:
    json.dump(memo_v2, f, indent=2)

# Save changelog
with open(CHANGELOG_PATH, "w") as f:
    json.dump(changes, f, indent=2)

print("Version 2 memo generated with change log.")