import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from helper.send_email import send_email

df = pd.read_excel("C:/Users/Tina L/OneDrive/Documents/Topper-Lynda/Week 1/Email Automation/data/job_offers.xlsx")
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'], errors='coerce')
COMPANY_NAME = "Awesome Solutions"

for _, row in df.iterrows():
    subject = f"Congratulations {row['CandidateName']}! Your Job Offer from {COMPANY_NAME}"
    body = f"""Dear {row['CandidateName']},

We are pleased to offer you the position of {row['JobRole']} at {COMPANY_NAME}.

Your joining date is {row['JoiningDate'].strftime("%d-%m-%Y")} and your CTC will be ₹{row['CTC']:,}.

Kindly confirm your acceptance by replying to this email.

We look forward to welcoming you on board.

Best Regards,
HR Team
{COMPANY_NAME}
"""
    send_email(row["Email"], subject, body)
    print(f"Sent offer to {row['CandidateName']} ({row['Email']})")
