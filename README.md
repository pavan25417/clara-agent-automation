# Clara Answers Automation Pipeline

Technical Assignment – ZenTrades AI

## Overview

This project implements a **zero-cost automation pipeline** that converts customer conversations into a deployable AI voice agent configuration.

The pipeline simulates how **Clara Answers** prepares and updates an AI receptionist for service trade businesses such as electricians, fire protection companies, and HVAC providers.

The system processes:

* **Demo call transcripts** → generates a preliminary AI agent configuration (v1)
* **Onboarding call transcripts** → updates the configuration with confirmed operational rules (v2)

The final output is a **versioned agent configuration with change tracking**.

---

# Architecture

The pipeline consists of two stages.

### Pipeline A — Demo Call → Preliminary Agent

Input:

```
inputs/demo_calls/demo_XXX.txt
```

Process:

1. Extract structured operational information
2. Generate an Account Memo JSON
3. Generate a Retell Agent Draft Spec

Output:

```
outputs/accounts/<account_id>/v1/
   account_memo.json
   retell_agent_spec.json
```

---

### Pipeline B — Onboarding Call → Agent Update

Input:

```
inputs/onboarding_calls/onboard_XXX.txt
```

Process:

1. Extract operational updates
2. Update the Account Memo
3. Generate Agent Spec v2
4. Record configuration changes

Output:

```
outputs/accounts/<account_id>/v2/
   account_memo.json
   retell_agent_spec.json
   changes.json
```

---

# Project Structure

```
clara_assignment

inputs
 ├ demo_calls
 │   └ demo_001.txt
 │
 └ onboarding_calls
     └ onboard_001.txt

outputs
 └ accounts
     └ account_001
         ├ v1
         │   ├ account_memo.json
         │   └ retell_agent_spec.json
         │
         └ v2
             ├ account_memo.json
             ├ retell_agent_spec.json
             └ changes.json

scripts
 ├ extract_demo_data.py
 ├ validate_memo.py
 ├ generate_agent_spec.py
 ├ update_to_v2.py
 ├ generate_agent_spec_v2.py
 └ run_pipeline.py
```

---

# How the Pipeline Works

1. The system reads demo call transcripts from:

```
inputs/demo_calls/
```

2. The script **extract_demo_data.py** converts the transcript into structured business data.

3. **generate_agent_spec.py** converts the structured memo into a **Retell agent configuration**.

4. When onboarding transcripts are processed, **update_to_v2.py** updates the memo and records configuration changes.

5. **generate_agent_spec_v2.py** regenerates the updated AI agent specification.

The entire process is executed through:

```
python scripts/run_pipeline.py
```

---

# How to Run the Project

### Step 1 — Clone the repository

```
git clone <repository-url>
cd clara_assignment
```

### Step 2 — Add transcripts

Place demo transcripts inside:

```
inputs/demo_calls/
```

Place onboarding transcripts inside:

```
inputs/onboarding_calls/
```

### Step 3 — Run the pipeline

```
python scripts/run_pipeline.py
```

### Step 4 — Check generated outputs

Outputs are stored in:

```
outputs/accounts/<account_id>/
```

Each account will contain both **v1** and **v2** agent configurations.

---

# Change Tracking

Configuration updates are recorded in:

```
changes.json
```

Example:

```
{
 "field": "business_hours",
 "old_value": "",
 "new_value": "Monday–Friday, Saturday",
 "reason": "Confirmed during onboarding call"
}
```

This ensures the system maintains **version history instead of overwriting data**.

---

# Design Principles

The system follows several safety and engineering principles:

### No Hallucination

Missing information is stored in:

```
questions_or_unknowns
```

instead of inventing values.

### Version Control

Agent configurations are stored in **v1 and v2 folders** to preserve history.

### Reproducibility

The entire pipeline can be executed with a single command.

### Zero-Cost Constraint

The solution relies only on:

* Python scripts
* Local JSON storage
* Transcript inputs

No paid APIs or services are required.

---

# Limitations

Current implementation uses **rule-based extraction** rather than a language model.

With production access, improvements would include:

* LLM-based information extraction
* Automatic speech-to-text processing
* CRM integrations (ServiceTrade / Jobber)
* Automated agent deployment via Retell API

---

# Demo

The pipeline demonstrates:

1. Demo call → Agent v1
2. Onboarding update → Agent v2
3. Change tracking between configurations

# Demo Video

Pipeline demo video:

https://drive.google.com/file/d/1O0T3pFjmulQfu1WNIWF6WRg0-vxSecUj/view?usp=sharing

---

# Author

B Pavan Manideep Reddy - 22BCI0293/NEO671768
Technical Internship Assignment – ZenTrades AI
