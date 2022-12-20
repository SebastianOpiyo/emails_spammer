from pymongo import MongoClient
import configuration

connection_params = configuration.connection_params




client = pymongo.MongoClient("mongodb+srv://spammer:spammer234@emailspammer.ybhsnef.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)
#connect to mongodb
# username --> spammer
# passwd --> spammer234
# mongoconnection = MongoClient(
#     'mongodb://{user}:{password}@{host}:'
#     '{port}/{namespace}?retryWrites=false'.format(**connection_params)
# )

# mongoconnection = MongoClient("mongodb+srv://spammer:spammer234@emailspammer.ybhsnef.mongodb.net/?retryWrites=true&w=majority")

# db = mongoconnection.databasename
