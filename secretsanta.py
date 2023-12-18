import smtplib
import random
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, secret_santa_name):
    subject = "Your Secret Santa Assignment"
    body = f"Hello,\n\nYou have been chosen as the Secret Santa for: {secret_santa_name}!\n\nHappy gifting!"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def secret_santa(participants, sender_email, sender_password):
    names_emails = participants.copy()
    # Shuffle the list of names for pairing
    random.shuffle(names_emails)

    # Pair each participant with someone else
    pairs = []
    for i in range(len(names_emails)):
        giver = names_emails[i]
        receiver = names_emails[(i + 1) % len(names_emails)]
        pairs.append((giver, receiver))

    # Send emails
    for giver, receiver in pairs:
        send_email(sender_email, sender_password, giver[1], receiver[0])

def read_participants_from_csv(file_path='secretsanta.csv'):
    participants = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            participants.append((row[0], row[1]))  # assuming first column is name, second is email
    return participants

sender_email = " " # add your sender email in the blanks
sender_password = " " # add your SMTP password (not your actual password) in the blanks
participants = read_participants_from_csv()
secret_santa(participants, sender_email, sender_password)
