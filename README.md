# AWS-Email-Sender

The Email Sender script simplifies the task of sending emails to a list of recipients from a text file.
It reads recipient details from the file, composes personalized messages if needed, and sends them via SMTP.
This automation tool is useful for bulk email communication, such as notifications, newsletters, or announcements.

# Usage Guide
Prerequisites:

Python 3.10+ installed on your system.
AWS account with Access Key and Secret Key for AWS Template Generator.
(most likely will want production mode on AWS account if not already requested).


# 1. AWS Template Generator:

Open Email-Template-Creator.py in a text editor.

Replace the placeholders for Access Key and Secret Key with your AWS IAM credentials.

Ensure that the boto3 and the colorama library is installed. If not, install it using pip install boto3, pip install colorama.

Run the .py in your fav environment (such as idle or pycharm or vsc).



# 2. Email Sender:

Open Mass-AWS-Sender.py in a text editor.

Replace the placeholders for Access Key and Secret Key with your AWS IAM credentials.

Update the commented credentials as per your email provider and template name.

Prepare your email list file (emails.txt) with a list of email addresses.

To start the Mass-AWS-Sender.py, simply run the provided .bat file




