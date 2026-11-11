import csv
from collections import Counter

input_file = "weekly_inventory_2026-11-12.csv"

valid_statuses = {
    "ACTIVE", "DISPUTE", "BANKRUPTCY",
    "CEASE", "HOLD7", "PAT-INS"
}

# Read source inventory
with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    accounts = list(reader)

# Identify duplicate account numbers
account_numbers = [
    row["credence_account_number"].strip()
    for row in accounts
]

counts = Counter(account_numbers)

valid_records = []
rejected_records = []

for row in accounts:

    errors = []

    if not row["client_id"].strip():
        errors.append("Missing client ID")

    if not row["client_account_number"].strip():
        errors.append("Missing client account number")

    account_no = row["credence_account_number"].strip()

    if not account_no:
        errors.append("Missing Credence account number")
    elif counts[account_no] > 1:
        errors.append("Duplicate Credence account number")

    try:
        balance = float(row["current_balance"])

        if balance < 0:
            errors.append("Negative account balance")

    except ValueError:
        errors.append("Invalid account balance")

    if row["account_status"].strip() not in valid_statuses:
        errors.append("Invalid account status")

    if errors:
        row["rejection_reason"] = "; ".join(errors)
        rejected_records.append(row)
    else:
        valid_records.append(row)

# Write validated records
with open("valid_inventory.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file, fieldnames=accounts[0].keys()
    )
    writer.writeheader()
    writer.writerows(valid_records)

# Write rejected records
with open("rejected_inventory.csv", "w", newline="") as file:
    fields = list(accounts[0].keys()) + ["rejection_reason"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rejected_records)

print("Inventory validation completed")
print("Total accounts:", len(accounts))
print("Valid accounts:", len(valid_records))
print("Rejected accounts:", len(rejected_records))