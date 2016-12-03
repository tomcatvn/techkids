coke = {
    "name" : "coke",
    "left" : 1,
    "price" : 7
    }

energy = {
    "name" : "energy",
    "left" : 2,
    "price" : 10,
    
    
    }

water = {
    "name" : "water",
    "left" : 3,
    "price" : 5
   
    
    }

vending_machine = {
    "button1" : coke,
    "button2" : energy,
    "button3" : water
    }

while True:
        button1 = input("press a button ")
        if button1 == "exit":
            break
        button = "button" + button1
        
        money = int(input("insert coin "))
           
        def buy(button,money):
            if vending_machine[button]["left"] <= 0:
                print("het do roi, ko mua duoc")
            elif vending_machine[button]["price"] > money:
                print ("thieu tien bo oi")
            elif vending_machine[button]["price"] == money:
                print("ban vua mua 1",vending_machine[button]["name"])
                vending_machine[button]["left"] -= 1
                print("con lai: ",vending_machine[button]["left"])
            elif vending_machine[button]["price"] < moneyx:
                print("ban vua mua 1",vending_machine[button]["name"])
                vending_machine[button]["left"] -= 1
                print("ban thua",money- vending_machine[button]["price"])
                print("con lai: ",vending_machine[button]["left"])
                

        buy(button,money)
    

        
    
