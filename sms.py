# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send_sms(message_text):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'ACafcfb95265aa8ed78f244127381a6a0f'
    auth_token = 'ee6d64c7d2feed220afebe1ad00a39f9'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=message_text,
                        from_='+19704708624',
                        to='+12132986849'
                    )
    print(message_text)

    print(message.sid)

