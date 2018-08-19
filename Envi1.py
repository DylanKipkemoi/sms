# add4dd431368dc4fea16c9fea42b39d47cbd3d0a579433aed63f1d053f

# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

# Specify your login credentials
username = "EnviExperts"
apikey = "add4dd431368dc4fea16c9fea42b39d47cbd3d0a579433aed63f1d053f"
# Specify the numbers that you want to send to in a comma-separated list
# Please ensure you include the country code (+254 for Kenya)
to = "+254704251165,+254716307755"
# And of course we want our recipients to know what we really do
message = "Hey.This is Vin(neCoder). He sent this SMS using Python.He is now working on customizing the sender id to suit the needs of different users e.g. schools,businesses,companies,saccos etc"
# Create a new instance of our awesome gateway class
gateway = AfricasTalkingGateway(username, apikey)
# *************************************************************************************
#  NOTE: If connecting to the sandbox:
#
#  1. Use "sandbox" as the username
#  2. Use the apiKey generated from your sandbox application
#     https://account.africastalking.com/apps/sandbox/settings/key
#  3. Add the "sandbox" flag to the constructor
#
#  gateway = AfricasTalkingGateway(username, apiKey, "sandbox");
# **************************************************************************************
# Any gateway errors will be captured by our custom Exception class below,
# so wrap the call in a try-catch block
try:
    # Thats it, hit send and we'll take care of the rest.

    results = gateway.sendMessage(to, message)

    for recipient in results:
        # status is either "Success" or "error message"
        print 'number=%s;status=%s;statusCode=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                          recipient['status'],
                                                                          recipient['statusCode'],
                                                                          recipient['messageId'],
                                                                          recipient['cost'])
except AfricasTalkingGatewayException, e:
    print 'Encountered an error while sending: %s' % str(e)
