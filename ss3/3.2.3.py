groceries = ["banana","orange","apple"]
stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear":15,
    }

prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
    }

def compute_bill(food):
    total = 0
    total += prices[food]
    print("+You are buying:",food)
    print(" price =",total)

def stock_list():
    for key,value in stock.items():
        print("   ",key,value)

print("our currently available stock:")
stock_list()

foodlist = ["pear","orange"]

for food in foodlist:
    if stock[food] > 0:
        compute_bill(food)
        stock[food] -=1
        print("  Remaining stock :")
        stock_list()
    else:
        print("+You are buying:",food)
        print("  Sorry, We are out of stock")

        
