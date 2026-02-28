import pymongo as py
client=py.MongoClient("mongodb://localhost:27017/")
db=client["Exercise"]
collection=db["Table 1"]

d=collection.delete_many({})
print(d.deleted_count)