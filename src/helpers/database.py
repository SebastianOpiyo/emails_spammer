import pymongo

#connect to mongodb
# username --> spammer
# passwd --> spammer234

client = pymongo.MongoClient("mongodb+srv://spammer:spammer234@emailspammer.ybhsnef.mongodb.net/?retryWrites=true&w=majority")
db = client.emailspammer

if db is not None:
    print("Database connected successfully")
else:
    print("Database not connected successfully")

