import csv

input_file = "valid_inventory.csv"

queues = {
    "ACTIVE": "phone_call_queue.csv",
    "HOLD7": "temporary_hold_queue.csv",
    "HOLD10": "temporary_hold_queue.csv",
    "CEASECALLS": "non_phone_communication_queue.csv",
    "CEASE": "no_communication_queue.csv",
    "PAT-INS": "insurance_billing_queue.csv",
    "DISPUTE": "restricted_review_queue.csv",
    "BANKRUPTCY": "restricted_review_queue.csv",
    "HOLD": "restricted_review_queue.csv"
}

files = {}
writers = {}

with open(input_file, "r", newline="", encoding="utf-8") as source:

    reader = csv.DictReader(source)
    headers = reader.fieldnames

    try:
        for queue_file in set(queues.values()) | {"review_queue.csv"}:
            output = open(queue_file, "w", newline="", encoding="utf-8")
            files[queue_file] = output

            writers[queue_file] = csv.DictWriter(
                output, fieldnames=headers
            )
            writers[queue_file].writeheader()

        total = 0

        for row in reader:
            status = row["account_status"].strip().upper()

            queue_file = queues.get(status, "review_queue.csv")

            writers[queue_file].writerow(row)
            total += 1

    finally:
        for output in files.values():
            output.close()

print("Account routing completed.")
print(f"Total accounts processed: {total}")