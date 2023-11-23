import random
from email.message import EmailMessage
import ssl
import smtplib
import os

def choose_book(path):
    with open(path,'r', encoding = 'utf-8') as books:
        list_of_books = []
        for row in books:
            list_of_books.append(row.strip())
    random_book = random.choice(list_of_books)
    return random_book

def send_email(book):
    sender = os.environ.get('SENDER')
    password = os.environ('PASSWORD')
    receiver = os.environ.get('RECEIVER')

    subject = 'Your book'
    body = f"""\
Hi!

I hope you're doing well.

Meanwhile, I hasten to inform you that the book that was drawn by me this time is:

"{book}"

Best regards!
    
"""

    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, em.as_string())
    return
