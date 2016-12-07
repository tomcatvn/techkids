import pymongo


# Config MongoDB


uri = "mongodb://admin:admin@ds119598.mlab.com:19598/cafeteria"


client = pymongo.MongoClient(uri)


db = client.get_default_database()


# Get MENU collection
menu_items = db["menu"].find()


menu_items_length = db["menu"].count()


order_items = db["order"].find()


order_items_length = db["order"].count()

for i in  range(order_items_length):
    for key, value in order_items[i].items():
        if key != "_id":
            print(key,value)
    print("---------------------")
tong = 0

for i in range(menu_items_length):
    for key, value in menu_items[i].items():
        if key != "_id":
            print(key,value)
    print("---------------------")
tong = 0

def checkhang(x):
    for t in range(menu_items_length):
        if menu_items[t]["name"] == x.capitalize():
            v= menu_items[t]["price"]
            
            return v


for i in range(order_items_length):
    print(order_items[i]["customer"])
    print(order_items[i]["order"])
    for x in order_items[i]["order"]:
        p = checkhang(x)
        tong += p
    print("TONG: ",tong)
    print("---------------------")
    tong = 0
        
    
