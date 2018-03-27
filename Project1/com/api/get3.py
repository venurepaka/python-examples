import requests
import json
import os



post_url='http://panama-webapps.stg.iro-panama.services.glb.prod.walmart.com/iro-panama/panama/postEvent';


file1 = open("inputPayload","r+")
payload1 =  file1.read()
payload1 = payload1.replace("1DDP2XNYTKED123","1DDP2XNYTKED456")
print payload1

# with open("inputPayload","w") as fileData:
#     fileData.write(payload1)


response = requests.post(post_url, headers={'Content-Type':'application/json'}, data=payload1);
jsonObj = json.loads(response.content);
print jsonObj

print jsonObj['status']

print json.dumps(jsonObj)