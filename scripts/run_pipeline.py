import os

print("Running Clara AI configuration pipeline...")

demo_folder = "../inputs/demo_calls"
demo_files = sorted([f for f in os.listdir(demo_folder) if f.endswith(".txt")])

for i, demo_file in enumerate(demo_files, start=1):

    account_id = f"account_{i:03d}"

    print(f"\nProcessing {demo_file} → {account_id}")

    os.environ["DEMO_FILE"] = demo_file
    os.environ["ACCOUNT_ID"] = account_id

    print("Step 1: Extract demo call data")
    os.system("python extract_demo_data.py")

    print("Step 2: Validate extracted memo")
    os.system("python validate_memo.py")

    print("Step 3: Generate agent specification v1")
    os.system("python generate_agent_spec.py")

    print("Step 4: Apply onboarding updates")
    os.system("python update_to_v2.py")

    print("Step 5: Generate agent specification v2")
    os.system("python generate_agent_spec_v2.py")

    print("Step 6: Generate summary report")
    os.system("python generate_summary.py")

print("\nPipeline completed successfully.")