import pymongo as py
client=py.MongoClient("mongodb://localhost:27017")
client.drop_database("CandidateDatabase")