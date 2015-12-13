#########################################
#This portion of the program sends an SMS
#message to the given number. This is one
#way the program will communicate with the
#user. Another potential way is through
#a push notification to a phone if this
#was a phone app.
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

    def send(self, number):
        """
        Sends SMS to a phone number corresponding to the number variable

        returns: nothing
        """
        self.message = self.client.messages.create(to="+19373295511", from_="+19378136340",
                                     body="Hello there!")
        self.receivedSMS=self.client.messages.list(To='19378136340')
        print self.receivedSMS

obj=send_SMS()
obj.send('+19373295511')