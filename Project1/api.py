import requests

getResp = requests.get("http://www.walmart.com")

print getResp.status_code

'''
getResp.encoding = 'ISO-8859-1'
outputfile = open("outfile.txt","w")
outputfile.write(str(getResp.text))
'''

