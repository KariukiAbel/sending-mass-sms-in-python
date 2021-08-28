import requests
import json

#mention url
url = "https://www.fast2sms.com/dev/bulk"

#create a dictionary
my_data = {
    #your default sender ID
    'sender_id':'FSTSMS',

     #put your mssage here
     'message':'Hi there, I am learning how to send a sms via python script',
     'language':'english',
     'route':'p',

     #you can send sms to multiple numbers separated by a comma
     'numbers':'254799179426, 254770557761, 254788603630' 
}

#create a dictionary
headers = {
    'authorization': 'YOUR API KEY HERE',
    'Content-Type':"application/x-www-form-urlencoded",
    'Cache-Control': "no-cache"
}

#make a post request
response = requests.request("POST",
                            url,
                            data=my_data,
                            headers= headers)

#load json data from source
returned_msg = json.loads(response.txt)

#print the send message
print (returned_msg['message'])