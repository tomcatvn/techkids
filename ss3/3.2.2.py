prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
    }
stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15
    }
price = 0
total = 0
for key,value in prices.items():
    print(key)
    print("price:",value)
for i in prices:
    price = prices[i] * stock[i]
    print(i," : price =",price)
    total += price
print("total price = ",total)
