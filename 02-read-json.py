import json

#Opening File
jsonFile = open("./public/json-sample.json")

#load the json data as JSON object
data = json.load(jsonFile)

#Iterating the JSON Object
for i in data['customers']:
    print(i)


#Close the file once finished the operation
jsonFile.close()
