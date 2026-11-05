menu = {"PIZZA" : 120,
        "BURGER" : 80,
        "FRIES" : 35,
        "COLA" : 20}
print("---Welcome to Our Restraunt!--- ")
print("Here is our menu :")
for item, price in menu.items() :
    print(f"-{item.capitalize()} : {price} EGP")
cart =[]
total = 0 
while True :
    order = input("What would you like to order ?(or type 'done' to finish) :").upper()
    if order == "DONE" :
        break
    elif order in menu :
        cart.append(order)
        total += menu[order]
        print(f"Added{order} to your cart. Current total: {total}EGP")
    else :
        print("Sorry, we dont have that item.Please choose from menu.")

print(f"\n---Your Final Bill---")
print("Items ordered :")
for item in cart :
    print(f"-{item} : {menu[item]} EGP")
print(f"Total Amount :{total}EGP")
print("Thankyou for visiting us!")
