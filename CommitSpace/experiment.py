import json
 
# Opening JSON file
f = open('save1')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# list
for i in data.saves:
    print(i)
 
# Closing file
f.close()