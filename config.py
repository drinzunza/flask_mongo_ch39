import pymongo
import certifi

me = {
    "name": "Sergio",
    "last_name": "Inzunza",
    "age": 37,
    "hobbies": [],
    "address": {
        "street": "evergreen",
        "city": "Springfield",
        "zip": 92830
    }
}

# database config
con_str = "mongodb+srv://FSDI:Test1234@cluster0.zn4fdae.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("organika")