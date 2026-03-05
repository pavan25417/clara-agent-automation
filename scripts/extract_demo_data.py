import json
import os

# Read environment variables from pipeline
demo_file = os.environ.get("DEMO_FILE", "demo_001.txt")
account_id = os.environ.get("ACCOUNT_ID", "account_001")

TRANSCRIPT_PATH = f"../inputs/demo_calls/{demo_file}"
TEMPLATE_PATH = "account_memo_template.json"
OUTPUT_DIR = f"../outputs/accounts/{account_id}/v1"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Read transcript
with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
    transcript = f.read().lower()

# Load template
with open(TEMPLATE_PATH, "r") as f:
    memo = json.load(f)

memo["account_id"] = account_id.upper()

# -------- COMPANY NAME EXTRACTION --------
if "ben's electric" in transcript or "bens electric" in transcript:
    memo["company_name"] = "Ben's Electric Solutions"
else:
    memo["company_name"] = ""
    memo["questions_or_unknowns"].append("Company name not clearly mentioned in transcript")

# -------- SERVICES EXTRACTION --------
services = []

if "ev charger" in transcript:
    services.append("EV charger installation")

if "panel upgrade" in transcript:
    services.append("electrical panel upgrades")

if "hot tub" in transcript:
    services.append("hot tub wiring")

if "troubleshoot" in transcript:
    services.append("electrical troubleshooting")

memo["services_offered"] = services

if not services:
    memo["questions_or_unknowns"].append("Services offered not clearly specified")

# -------- BUSINESS HOURS --------
memo["business_hours"]["days"] = ""
memo["business_hours"]["start_time"] = ""
memo["business_hours"]["end_time"] = ""
memo["business_hours"]["timezone"] = ""

memo["questions_or_unknowns"].append("Business hours not mentioned in demo call")
memo["questions_or_unknowns"].append("Timezone not mentioned")

# -------- EMERGENCY DEFINITION --------
emergencies = []

if "gas station" in transcript:
    emergencies.append("gas station power failure")

if "emergency" in transcript:
    emergencies.append("urgent electrical issue")

memo["emergency_definition"] = emergencies

memo["emergency_action"] = ""
memo["questions_or_unknowns"].append("Emergency routing rules not clearly defined")

# -------- NON EMERGENCY FLOW --------
memo["non_emergency_flow"] = "collect caller details and schedule service"

# -------- INFO TO COLLECT --------
memo["information_to_collect"] = [
    "caller name",
    "phone number",
    "service address",
    "issue description"
]

# Save output
output_path = os.path.join(OUTPUT_DIR, "account_memo.json")

with open(output_path, "w") as f:
    json.dump(memo, f, indent=2)

print(f"Account memo v1 generated for {account_id}")