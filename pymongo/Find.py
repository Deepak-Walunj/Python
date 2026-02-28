import pymongo as py

client=py.MongoClient("mongodb://localhost:27017/")
db=client["Exercise"]
collection=db["Table 1"]
# print(collection)
many=collection.find({'Age':35},{"_id":0})
for i in many:
    print(i)
one =collection.find_one({"Age":35},{"_id":0})
print(one)