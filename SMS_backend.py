#########################################
#This portion of the program sends an SMS
#message to the given number. This is one
#way the program will communicate with the
#user. Another potential way is through
#a push notification to a phone if this
#was a phone app.
import twilio.rest import TwilioRestClient


class send_SMS():
    """
    Uses Twilio to send an SMS to a given number
    """
    account_sid = "AC7162b52b47f7383aec3ad400e9cc40e4"
    auth_token = "c4dbfa0c3ed665fd699eac2f99d4976e"
    client = TwilioRestClient(account_sid, auth_token)

    def __init__(self):
        """
        Intializes variables
        """
        self.account_sid = "AC7162b52b47f7383aec3ad400e9cc40e4"
        self.auth_token = "c4dbfa0c3ed665fd699eac2f99d4976e"
        self.client = TwilioRestClient(aself.ccount_sid, self.auth_token)

    def send(self, number):
        """
        Sends SMS to a phone number corresponding to the number variable

        returns: nothing
        """
        message = client.messages.create(to="+19373295511", from_="+15555555555",
                                     body="Hello there!")