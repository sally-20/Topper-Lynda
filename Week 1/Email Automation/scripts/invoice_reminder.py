import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo
from helper.send_email import send_email

df = pd.read_excel(r"C:\Users\Tina L\OneDrive\Documents\Topper-Lynda\Week 1\Email Automation\data\customer_invoices.xlsx")
today = datetime.now(ZoneInfo("Asia/Kolkata")).date()
df["InvoiceDueDate"] = pd.to_datetime(df["InvoiceDueDate"]).dt.date

for _, row in df.iterrows():
    days_left = (row["InvoiceDueDate"] - today).days

    # Friendly deadline note
    if days_left > 1:
        deadline_note = f"{days_left} days left until your invoice is due."
        subject_tag   = f"{days_left} days"
    elif days_left == 1:
        deadline_note = "1 day left until your invoice is due."
        subject_tag   = "1 day"
    elif days_left == 0:
        deadline_note = "Your invoice is due **today**."
        subject_tag   = "Today"
    else:
        deadline_note = f"Your invoice is overdue by {-days_left} day(s). Please pay immediately."
        subject_tag   = "Overdue"

    subject = f"Invoice Reminder ({subject_tag}) - {row['CustomerName']}"

    body = f"""Dear {row['CustomerName']},

This is a reminder that your invoice of ₹{row['InvoiceAmount']:,} is scheduled for {row['InvoiceDueDate']:%d-%m-%Y}.

{deadline_note}

Kindly make the payment at your earliest convenience.

Regards,
Finance Team
"""

    send_email(row["Email"], subject, body)
    print(f"Sent to {row['CustomerName']} ({row['Email']}) – {deadline_note}")
