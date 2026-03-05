import os
import json

OUTPUT_DIR = "../outputs/accounts"
SUMMARY_PATH = "../outputs/summary_report.json"

accounts_summary = []

for account in sorted(os.listdir(OUTPUT_DIR)):

    account_path = os.path.join(OUTPUT_DIR, account)

    v2_memo_path = os.path.join(account_path, "v2", "account_memo.json")

    if os.path.exists(v2_memo_path):

        with open(v2_memo_path, "r") as f:
            memo = json.load(f)

        account_info = {
            "account_id": memo.get("account_id", account),
            "company_name": memo.get("company_name", ""),
            "services_detected": len(memo.get("services_offered", [])),
            "unknown_fields": len(memo.get("questions_or_unknowns", [])),
            "version_generated": "v2"
        }

        accounts_summary.append(account_info)

summary = {
    "total_accounts_processed": len(accounts_summary),
    "accounts": accounts_summary
}

with open(SUMMARY_PATH, "w") as f:
    json.dump(summary, f, indent=2)

print("Summary report generated successfully.")