import json
import os

# Paths
MEMO_V2_PATH = "../outputs/accounts/account_001/v2/account_memo.json"
TEMPLATE_PATH = "retell_agent_template.json"
OUTPUT_DIR = "../outputs/accounts/account_001/v2"

# Load v2 memo
with open(MEMO_V2_PATH, "r") as f:
    memo = json.load(f)

# Load template
with open(TEMPLATE_PATH, "r") as f:
    agent = json.load(f)

# Fill fields
agent["agent_name"] = "SafeSprinkler AI Receptionist"
agent["version"] = "v2"
agent["company_name"] = memo["company_name"]

agent["greeting_message"] = (
    f"Hello, thank you for calling {memo['company_name']}. "
    "How can I assist you today?"
)

agent["business_hours_logic"] = (
    "During business hours the AI assists customers normally. "
    "If the caller reports an emergency, transfer to the on-call technician."
)

agent["after_hours_logic"] = (
    "Outside business hours ask if the issue is an emergency. "
    "If not, collect details and inform the customer the team will respond next business day."
)

agent["emergency_flow"] = (
    "If the caller mentions sprinkler pipe burst, heavy leak, or fire alarm trigger, "
    "attempt to transfer the call to the on-call technician for up to 90 seconds."
)

agent["non_emergency_flow"] = memo["non_emergency_flow"]

agent["information_to_collect"] = memo["information_to_collect"]

agent["fallback_behavior"] = (
    "If transfer fails after 90 seconds, collect caller information and notify technician."
)

agent["notes"] = memo["notes"]

# Save output
output_path = os.path.join(OUTPUT_DIR, "retell_agent_spec.json")

with open(output_path, "w") as f:
    json.dump(agent, f, indent=2)

print("Retell agent spec v2 generated successfully.")