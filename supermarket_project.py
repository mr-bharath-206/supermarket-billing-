from datetime import datetime

name = input("Enter your name: ")
#List of items
lists = '''
list of items        price per kg 
1. rice              30
2. wheat flour       36
3. sugar             40
4. pulses            50
5. salt              10
6. tea powder        120
7. coffee powder     200
'''
#declaration
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []

#rates
option = input("Press enter to see the list of items: ")
if option == "":
    print(lists)
items = {'rice': 30, 'wheat flour': 36, 'sugar': 40, 'pulses': 50, 'salt': 10, 'tea powder': 120,'coffee powder': 200}
for i in range(len(items)):
    inpu = int(input("Enter 0 to exit or 1 to buy an item: "))
    if inpu == 0:
        print("Thank you for visiting the supermarket!")
        break
    if inpu == 1:
        item = input("Enter the item you want to buy:")
        Quantity = int(input("Enter the quantity in kg:"))
        if item in items.keys():
            price = Quantity * items[item]
            pricelist.append((item, items, Quantity, price))
            totalprice += price
            ilist.append(item)
            qlist.append(Quantity)
            plist.append(price)
            gst = (totalprice *5) / 100
            finalprice = totalprice + gst
        else:
            print("Item not available in the supermarket.")
    else:
        print("Invalid input. Please try again.")
    inp = input("Do you want to bill the items? (yes/no): ")
    if inp=='yes':
     pass
     if finalprice != 0:
        print(25*"=","Bharath Supermarket",26*"=")
        print(28*" ","HYDERABAD")
        print("Name:", name, 30*" ", "Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(72*"_")
        print("S.no",3*" ","ITEMS",10*' ',"Quantity", 10*" ","Price")
        for i in range(len(pricelist)):
            print(i,6*" ",ilist[i],14*" ",qlist[i],15*" ",plist[i])
        print(72*"_")
        print(45*" ","Total Price:",'Rs', totalprice)
        print(72*"_")
        print(53*" ","GST:",'Rs', gst)
        print(72*"_")
        print(45*" ","Final Price:",'Rs', finalprice)
        print(72*"_")
        print(14*"=","Thank you for visiting the supermarket!",17*"=")