import csv

path = r"/home/ajit/pd/Patient_Debt_Payment_Records.csv"
path1 = r"/home/ajit/pd/Patient_Debt_Payment_Records1.csv"

with open(path, mode="r", encoding="UTF-8", newline="") as file:

    reader = csv.DictReader(file)

    with open(path1, mode="w", encoding="UTF-8", newline="") as wf:

        fieldnames = reader.fieldnames

        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            row['Patient Account ID'] = str(row['Patient Account ID'])
            row['Original Debt Amount'] = float(row['Original Debt Amount'])
            row['Payment Received'] = float(row['Payment Received'])

            writer.writerow(row)

print("File written successfully!")
