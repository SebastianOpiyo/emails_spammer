from pymongo import MongoClient
import pymongo
import configuration

connection_params = configuration.connection_params




client = pymongo.MongoClient("mongodb+srv://spammer:spammer234@emailspammer.ybhsnef.mongodb.net/?retryWrites=true&w=majority")
db = client.emailspammer

if db is not None:
    print("Database connected successfully")
else:
    print("Database not connected successfully")

#connect to mongodb
# username --> spammer
# passwd --> spammer234
# mongoconnection = MongoClient(
#     'mongodb://{user}:{password}@{host}:'
#     '{port}/{namespace}?retryWrites=false'.format(**connection_params)
# )

# mongoconnection = MongoClient("mongodb+srv://spammer:spammer234@emailspammer.ybhsnef.mongodb.net/?retryWrites=true&w=majority")

# db = mongoconnection.databasename
