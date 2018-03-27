import requests
import json

#wm_url = "http://itemsetupquerysvc.stg.nxgensearch.catdev.qa.walmart.com/item-setup-query-service-app/services/master-item/v1?identifierType=OFFER&id=B6259DCAF75B419EB3E0A3214DFA53CB&fields=PRODUCT%2COFFER%2CLOGISTICS";

wm_url = "http://itemstoresetup.stg0.itemstore.catdev.glb.prod.walmart.com/itemstore-item-setup-app/services/offer/ABFA852428DB4CCE9E1AE8C9F9EA7355";

wm_ptu = requests.get(wm_url)
print wm_ptu
wm_jsondata = json.loads(wm_ptu.content)
#print json.dumps(wm_jsondata);
print wm_jsondata['status']
print wm_jsondata['payload']['offerId']


assert('ABFA852428DB4CCE9E1AE8C9F9EA7355' == wm_jsondata['payload']['offerId'])

if 'ABFA852428DB4CCE9E1AE8C9F9EA7355' == wm_jsondata['payload']['offerId']:
    print 'offerId is true'

print 'done'



