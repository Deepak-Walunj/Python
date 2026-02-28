import pymongo as py

client=py.MongoClient("mongodb://localhost:27017/")
db=client["Exercise"]
collection=db["Table 1"]
# dict=[{
#     "Name":"John Doe",
#     "Age":30,
#     "Gender":"Male",
#     "Occupation":"Engineer"},
#     {
#     "Name":"Jane Smith",
#     "Age":28,
#     "Gender":"Female",
#     "Occupation":"Doctor"},
#     {
#     "Name":"David Johnson",
#     "Age":35,
#     "Gender":"Male",
#     "Occupation":"Teacher"}
#     ]

# collection.insert_many(dict)

dict2 = {
    "Name":" Smith",
    "Age":35,
    "Gender":"Male",
    "Occupation":"Engineer"}

collection.insert_one(dict2)