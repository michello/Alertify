from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACbb4b9650631364e99781ded800fa9699" 
auth_token = "0a068601c149167e134887defd6fc2a9" 
client = TwilioRestClient("ACbb4b9650631364e99781ded800fa9699", \
                          "0a068601c149167e134887defd6fc2a9")
#account_sid, auth_tokens

client.messages.create(to="+19176671977", from_="+16464193165",
                                     body="Hello there!")
