import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo
from helper.send_email import send_email

df = pd.read_excel(r"C:\Users\Tina L\OneDrive\Documents\Topper-Lynda\Week 1\Email Automation\data\emi_schedule.xlsx")
today = datetime.now(ZoneInfo("Asia/Kolkata")).date()
df["EMIDueDate"] = pd.to_datetime(df["EMIDueDate"]).dt.date

for _, row in df.iterrows():
    days_left = (row["EMIDueDate"] - today).days
    if days_left > 1:
        deadline_note = f"{days_left} days left until your EMI is due."
    elif days_left == 1:
        deadline_note = "1 day left until your EMI is due."
    elif days_left == 0:
        deadline_note = "Your EMI is due **today**."
    else:
        deadline_note = f"Your EMI is overdue by {-days_left} day(s). Please pay immediately."

    subject = f"EMI Reminder - Loan {row['LoanAccountNumber']} ({deadline_note.split()[0]})"
    body = f"""Dear {row['CustomerName']},

This is a reminder that your EMI of ₹{row['EMIAmount']:,} for Loan Account Number {row['LoanAccountNumber']} is scheduled for {row['EMIDueDate']:%d-%m-%Y}.

{deadline_note}

Kindly ensure the payment is made to avoid penalties.

Regards,
Bank Loan Department
"""

    send_email(row["Email"], subject, body)
    print(f"Sent to {row['CustomerName']} ({row['Email']}) – {deadline_note}")
