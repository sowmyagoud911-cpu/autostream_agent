import json
import os

LEADS_FILE = "leads.json"


def mock_lead_capture(name, email, platform):
    lead = {
        "name": name,
        "email": email,
        "platform": platform
    }

    # If file exists → load existing data
    if os.path.exists(LEADS_FILE):
        with open(LEADS_FILE, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []
    else:
        data = []

    # Append new lead
    data.append(lead)

    # Save back to file
    with open(LEADS_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\n✅ Lead captured successfully: {name}, {email}, {platform}\n")