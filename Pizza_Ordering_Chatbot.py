print("Hello, my name is Alex your virtual assitant. I will help you order a pizza! ")
print("I am going to ask you a few questions. Please press enter after each answer.")
userName = input("\nEnter your name:  ")
while (len(userName) == 0):
        userName = input("Oh No! Name cannot be blank please enter your name:  ")

if userName.lower() == "dee":
    print("\nMy creator," + userName + ". Pleasure to serve you!")
else:
   print("\nHello, "   +  userName + ". Nice to meet you!")

keepGoing = "y"
while keepGoing.lower() == "y":
    size = input("\nWhat size do you want to order?  Enter small, medium, or large:  ")
    while size.lower() != "small" and size.lower() != "medium" and size.lower() != "large":
        size = input("That is not a valid value. Please enter small, medium, or large:  ")
    while (len(size) == 0):
            size = input("Oh No! Size cannot be blank please enter small, medium or large:  ")
    flavor = input("\nEnter the flavor of pizza:  ")
    while (len(flavor) == 0):
            flavor = input("Oh No! Flavor cannot be blank please enter a flavor of pizza to enjoy! :  ")
    if flavor == "pineapple":

      print("Yuck! PINEAPPLES DO NOT BELONG ON PIZZA! But Enjoy! LOL!")  
    crustType = input("\nWhat type of crust would you like?:  ")
    while (len(crustType) == 0):
            crustType = input("Oh No! Crust Type cannot be blank. Please enter a Crust Type,for example; garlic or stuffed?:  ")
    quantity = input("\nHow many pizzas would you like to order? Enter a numeric value:  ")
    while (len(quantity) == 0):
            quantity = input("Oh No! Quantity cannot be blank. Please enter the number value of pizzas you would like to order.:  ")
    while not quantity.isdigit():
        quantity = input("\nThis value is not recognized. Please enter a numeric value (i.e. 1234):  ")
    quantity = int(quantity)
    method = input("\nWill it be carry out or delivery?:  ")
    while method.lower() != "delivery" and method.lower() != "carry out" and method.lower != "carryout":
      while (len(method) == 0):
            method = input("Oh No! Method cannot be blank. Will it be carry-out or delivery?:  ")

    salesTax = 1.1

    if size.lower() == "small":
        pizzaCost = 8.99
    elif size.lower() == "medium":
        pizzaCost = 14.99
    elif size.lower() == "large":
        pizzaCost = 17.99

    if method.lower() == "delivery":
            deliveryFee = 5
    else:
           deliveryFee = 0
    total = (pizzaCost * quantity) * salesTax + deliveryFee

    print("\n----------------")
    print("Thank You,", userName,",for your order.")
    print("Your",quantity,size,flavor,"pizzas with",crustType,"crust costs","${:,.2f}".format(total) + ".")
    if total >= 50:
        print("\nCongratulations!, you've been awarded a $10 off coupon for your next order!")
    else:
        print("\nOrders over $50 will recieve a free $10 off coupon!")
    print("----------------")

    print("Perfect! Your order has been recieved! ETA is 5 minutes!")

    for min in range(3, 1, -1):
        print(min, "minutes remaining")
        for seconds in range(60, 0, -1):
            print(seconds, end = "  \r")
            import time 
            time.sleep(1) 

    print("Great News! Your order is ready!")

    keepGoing = input("Would you like to place another order? Enter yes or no:  ")