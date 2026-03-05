import json

MEMO_PATH = "../outputs/accounts/account_001/v1/account_memo.json"

required_fields = [
    "company_name",
    "services_offered",
    "business_hours",
    "emergency_definition",
    "emergency_action",
    "information_to_collect"
]

with open(MEMO_PATH, "r") as f:
    memo = json.load(f)

missing = []

for field in required_fields:
    if not memo.get(field):
        missing.append(field)

if missing:
    memo["questions_or_unknowns"].extend(
        [f"Missing information: {field}" for field in missing]
    )

    with open(MEMO_PATH, "w") as f:
        json.dump(memo, f, indent=2)

    print("Missing information detected and recorded.")
else:
    print("All required fields present.")