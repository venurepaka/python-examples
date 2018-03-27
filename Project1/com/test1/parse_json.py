import json
import os

jsonData = '{"name": "Frank123", "age": 39}'
jsonToPython = json.loads(jsonData)

print jsonToPython["name"]

# nm = str(jsonToPython["name"])
# #print nm
#
# outputFile = open("name.txt", "wb");
# outputFile.write(nm);
# outputFile.close();
#
# outputFile = open("name.txt", "r+");
# print outputFile.read()
#
# #os.remove("name.txt")