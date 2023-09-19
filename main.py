Timport datetime
from twilio.rest import Client 

# Twilio credentials
account_sid = 'INSERT_HERE'
auth_token = 'INSERT_HERE'
client = Client(account_sid, auth_token)

# Your phone number
my_number = '+18138415935'

# set the reminder day
reminder_day = 8

while True:
    today = datetime.date.today()
    now = datetime.datetime.now
    if (today.day == reminder_day) and (now.hour == 15 and now.minute == 0):
        message = client.messages.create(
                              messaging_service_sid='SM65faddee750367da23b6a6298b82e266',
                              body='This is your monthly reminder to pay your credit card bill!',
                              to=my_number
                          )
        print(message.sid)

    # Run every minute  
    datetime.sleep(7*24*60*60)
