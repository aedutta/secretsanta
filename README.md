# Secret Santa
A fun and confidential way to organize Secret Santa during the holidays!

## Introduction
This Secret Santa program is ideal if you're looking for a fun and anonymous method to run a Secret Santa exchange within your friend group or family. The program automates the assignment process and sends out emails without anyone needing to know who's been assigned to whom.

## Getting Started
I used the ``stmplib`` package to send out emails to people from a ``secretsanta.csv`` list. Here are the steps to run this by yourself:
1. Clone the repository.
2. Change the ``secretsanta.csv`` with the names and emails of your friends.
3. Create an email account that will send the emails. Maybe something like ``secretsanta@hoho.com``. This account will send all the assignments to everyone and you won't have to look at the assignments unless you really want to.
4. Enable two-factor authentication for the email account. Then, generate an SMTP password. You can follow the instructions here: [Gmail SMTP setup guide](https://www.gmass.co/blog/gmail-smtp/).
5. Modify ``secretsanta.py`` to include the sender email and SMTP password.
6. Run the program.
