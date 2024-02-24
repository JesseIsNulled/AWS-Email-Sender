import boto3

#           __  __                       
#     ____ |  \/  |                      
#    / __ \| \  / | __ _ ___  ___  _ __  
#   / / _` | |\/| |/ _` / __|/ _ \| '_ \ 
#  | | (_| | |  | | (_| \__ \ (_) | | | |
#   \ \__,_|_|  |_|\__,_|___/\___/|_| |_|
#    \____/                              
#                                       



# Initialize
client = boto3.client(
    'ses',
    aws_access_key_id='YOUR_KEY_HERE',
    aws_secret_access_key='YOUR_KEY_HERE',
    region_name='us-east-2'
)

# Define the email template content, this is permanent so do your HTML testing first.
template_content = {
    'Template': {
        'TemplateName': 'Custom', #Template name goes here. This will be permanent in your template on AWS
        'SubjectPart': 'Test Email', #Subject of the email goes here.
        'TextPart': 'Hello, this is a test email.', 
        'HtmlPart': '<html><body><h1>Hello, this is a test email.</h1></body></html>'
    }
}

# Create the email template
response = client.create_template(**template_content)

# Print the response
print(response)
