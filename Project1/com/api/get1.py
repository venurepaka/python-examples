import requests
import json
import os

# wm_url = "http://itemsetupquerysvc.stg.nxgensearch.catdev.qa.walmart.com/item-setup-query-service-app/services/master-item/v1?identifierType=OFFER&id=B6259DCAF75B419EB3E0A3214DFA53CB&fields=PRODUCT%2COFFER%2CLOGISTICS";

# wm_url = "http://itemstoresetup.stg0.itemstore.catdev.glb.prod.walmart.com/itemstore-item-setup-app/services/offer/ABFA852428DB4CCE9E1AE8C9F9EA7355";
#
# wm_ptu = requests.get(wm_url)
#
# print wm_ptu
# wm_jsondata = json.loads(wm_ptu.content)
# print wm_jsondata

post_url='http://panama-webapps.stg.iro-panama.services.glb.prod.walmart.com/iro-panama/panama/postEvent';
# payload = [
# {
#      "product_id":"1DDP2XNYTKED123",
#      "vertical_id": 0,
#      "locale_id": "en_US",
#      "bu_id": 0,
#      "mart_id": 0
#
#    }
# ];

file1 = open("inputPayload","r")
payload1 =  file1.read()

# data2 = json.dumps(payload)

response = requests.post(post_url, headers={'Content-Type':'application/json'}, data=payload1);
jsonObj = json.loads(response.content);
print jsonObj

print jsonObj['status']

print json.dumps(jsonObj)