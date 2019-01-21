# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send_sms(message_text):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=message_text,
                        from_='+',
                        to='+'
                    )
    print(message_text)

    print(message.sid)

