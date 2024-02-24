import boto3
from colorama import Fore, Back, Style

#           __  __                       
#     ____ |  \/  |                      
#    / __ \| \  / | __ _ ___  ___  _ __  
#   / / _` | |\/| |/ _` / __|/ _ \| '_ \ 
#  | | (_| | |  | | (_| \__ \ (_) | | | |
#   \ \__,_|_|  |_|\__,_|___/\___/|_| |_|
#    \____/                              
#                                       


# Initialize the SES client with your access key and secret key
client = boto3.client(
    'ses',
    aws_access_key_id='YOUR_KEY_HERE',
    aws_secret_access_key='YOUR_KEY_HERE',
    region_name='us-east-2'
)

# Initialize the colorama library
print(Fore.GREEN + 'Starting to send emails...' + Style.RESET_ALL)

# Open the .txt file and read the email addresses, the txt doesnt needs to be in the folder with the .py
with open('emails.txt', 'r') as f:
    email_addresses = [line.strip() for line in f.readlines()]

# Define the email template data as a string
template_data = '{"name": "Recipient Name", "message": "Hello from AWS SES!"}'#Leave this alone

# Send the email to each recipient
for recipient in email_addresses:
    try:
        response = client.send_templated_email(
            Source='contact@example.com',#Sender Email
            Destination={'ToAddresses': [recipient]},
            Template='Example_Template',#Choose which template name you will send from https://us-east-2.console.aws.amazon.com/ses/home?region=us-east-2#/email-templates
            TemplateData=template_data,
            ReplyToAddresses=['contact@example.net']
        )
        print(Fore.GREEN + f"Sent email to {recipient}: {response}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error sending email to {recipient}: {e}" + Style.RESET_ALL)

print(Fore.GREEN + 'Finished sending emails.' + Style.RESET_ALL)
