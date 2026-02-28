import pymongo as py
client=py.MongoClient("mongodb://localhost:27017/")
db=client["Exercise"]
coll=db["Table 1"]
coll.drop()
