import json
import os

# Paths
MEMO_PATH = "../outputs/accounts/account_001/v1/account_memo.json"
TEMPLATE_PATH = "retell_agent_template.json"
OUTPUT_DIR = "../outputs/accounts/account_001/v1"

# Load account memo
with open(MEMO_PATH, "r") as f:
    memo = json.load(f)

# Load template
with open(TEMPLATE_PATH, "r") as f:
    agent = json.load(f)

# Fill agent spec fields
agent["agent_name"] = "SafeSprinkler AI Receptionist"
agent["version"] = "v1"
agent["company_name"] = memo["company_name"]

agent["greeting_message"] = (
    f"Hello, thank you for calling {memo['company_name']}. "
    "How can I assist you today?"
)

agent["business_hours_logic"] = (
    "If the caller needs assistance during business hours, help them "
    "or transfer the call if it is an emergency."
)

agent["after_hours_logic"] = (
    "If the call happens outside business hours, ask the caller if it is an emergency. "
    "If not, collect their details and inform them the team will respond next business day."
)

agent["emergency_flow"] = (
    "If the caller describes an emergency such as sprinkler burst, heavy leak, "
    "or active fire alarm trigger, immediately transfer the call to the on-call technician."
)

agent["non_emergency_flow"] = memo["non_emergency_flow"]

agent["information_to_collect"] = memo["information_to_collect"]

agent["fallback_behavior"] = (
    "If the call transfer fails, apologize to the caller and collect their details "
    "so the technician can call them back."
)

agent["notes"] = "Generated automatically from account memo."

# Save output
output_path = os.path.join(OUTPUT_DIR, "retell_agent_spec.json")

with open(output_path, "w") as f:
    json.dump(agent, f, indent=2)

print("Retell agent spec v1 generated successfully.")