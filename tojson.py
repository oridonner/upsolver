import glob
import json

x =  '{}'
z = json.loads(x)
files = glob.glob("/home/air/upsolver/config/*")
for file in files:
    #print(file)
    # print(value.read())
    
    # load json file
    # calculate value
    value = open(file, "r")
    y = {file: value.read()}
    #print (y)
    # update value
    z.update(y)
    
print(z)

# def validateJSON(jsonData):
#     try:
#         json.loads(jsonData)
#     except ValueError as err:
#         return False
#     return True

# result=validateJSON(z)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(z, f, ensure_ascii=False, indent=4)

