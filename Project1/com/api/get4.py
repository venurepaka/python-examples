import requests
import json

payload = {'identifierType': 'OFFER', 'id': 'B6259DCAF75B419EB3E0A3214DFA53CB','fields':'PRODUCT'}
headerParams = {'WM_SVC.VERSION': '0.0.1', 'WM_SVC.NAME': 'item-setup-query-service-app','WM_QOS.CORRELATION_ID':'546a5b97-dd86-4273-9008-e111455b4504','WM_SVC.ENV':'stg0','WM_CONSUMER.ID':'9ce3f2a8-e087-46bf-8c73-54a72d99c165','Accept':'application/json','external':'true'}


getResponse = requests.get('http://itemsetupquerysvc.stg.nxgensearch.catdev.qa.walmart.com/item-setup-query-service-app/services/master-item/v1?',
                           params=payload, headers=headerParams)

print getResponse.content