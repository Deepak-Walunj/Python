import pymongo as py
client=py.MongoClient("mongodb://localhost:27017/")
db=client["Exercise"]
collection=db["Table 1"]
prev={"Name":"David Johnson"}
nxt={"$set":{"Occupation":"Pornstar"}}
collection.update_one(prev,nxt)

up=collection.update_many(prev,nxt)
print(up.modified_count)