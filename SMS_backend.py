'''
This portion of the program sends an SMS
message to the given number. This is one
way the program will communicate with the
user. Another potential way is through
a push notification to a phone if this
was a phone app. I noticed that Chrome
supports browser based push notifications
that are really nice and non obtrusive.
Maybe use that instead.
'''
#TODO: 2 Figure out how Facebook sends push notification to the browser. This might go under web_frontend.py
#TODO: 1 Return the status of each message sent. This would be higher priority in product sold for money.
from twilio.rest import TwilioRestClient

class send_SMS():
    """
    Uses Twilio to send an SMS to a given number
    """

    def __init__(self):
        """
        Intializes self.client which is responsible for sending and receiving SMS in Twilio
        """
        self.account_sid = "AC7162b52b47f7383aec3ad400e9cc40e4"
        self.auth_token = "c4dbfa0c3ed665fd699eac2f99d4976e"
        self.client = TwilioRestClient(self.account_sid, self.auth_token)

    def send(self, number, SMSbody):
        """
        Sends SMS to a phone number corresponding to the number variable

        takes: number in the "+1XXXXXXX" format. SMSbody which should be <140 characters
        returns: nothing
        """
        self.message = self.client.messages.create(to="+19373295511", from_="+19378136340" body=SMSbody)
        self.receivedSMS = self.client.messages.list(To='19378136340')
        print self.receivedSMS

obj=send_SMS()
obj.send('+19373295511')