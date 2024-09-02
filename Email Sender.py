import os
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
from dotenv import load_dotenv
# import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the environment variable
# password = os.getenv('pass')
# print("Password:", password)



# email sender and the password
email_sender = ''
email_password = ""

# the subject of the email
subject = 'Internship Application Approval'

#email body template with placeholder for recipient name
body_template = (
    "Dear {name},\n\n"
    "Congratulation We are pleased to inform you that your application for the internship position at Tech Innovators Inc. has been successfully approved. "
    "We were impressed with your qualifications and believe you will be a great addition to our team. "
    "Please find the attached document with further details regarding the next steps, including start dates and onboarding information.\n\n"
    "Should you have any questions or require further information, do not hesitate to reach out to us. "
    "We look forward to working with you.\n\n"
    "Best regards,\n"
    "\n"
    "HR Manager\n"
    "Tech Innovators Inc.\n"
    "\n"
    "Tech City, TC 45678\n"
    "(123) 456-7890\n"
    "hr@techinnovators.com\n"
    "www.techinnovators.com"
)

# reading Excel file
csv_path = r"C:\Users\hp\Downloads\multiple_emails.xlsx"
emails_df = pd.read_excel(csv_path)

# Check for any missing data
print("Missing data in 'Receiver', 'Attatchment', or 'Names':")
print(emails_df[emails_df[['Receiver', 'Attatchment', 'Names']].isna().any(axis=1)])

# Looping through the Excel file and sending emails with attachments
for index, row in emails_df.iterrows():
    try:
        email_receiver = row['Receiver']
        attachment_file_name = row['Attatchment']
        recipient_name = row['Names']

        print(f"Processing row {index}: Receiver = {email_receiver}, Attachment = {attachment_file_name}, Name = {recipient_name}")

        # Define email parameters
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject

        # Personalize the email body with the recipient's name
        body = body_template.format(name=recipient_name)
        em.set_content(body)

        # Set the email as multipart before adding attachments
        em.make_mixed()

        # Attach the document
        with open(attachment_file_name, 'rb') as attachment_file:
            file_data = attachment_file.read()
            file_name = attachment_file.name.split("\\")[-1]

        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(file_data)
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
        em.attach(attachment)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    except KeyError as e:
        print(f"KeyError: {e} in row {index}")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e} for attachment {attachment_file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
