print("Hello, my name is Alex your virtual assitant. I will help you order a pizza! ")
print("I am going to ask you a few questions. Please press enter after each answer.")
userName = input("\nEnter your name:  ")
print("\nHello, "   +  userName +". Nice to meet you!")

size = input("\nWhat size do you want to order?  Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of pizza:  ")
crustType = input("\nWhat type of crust would you like?:  ")
quantity = input("\nHow many pizzas would you like to order? Enter a numeric value:  ")
quantity = int(quantity)
method = input("\nWill it be carry out or delivery?:  ")

salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax

print("\n----------------")
print("Thank You,", userName,",for your order.")
print("Your",quantity,size,flavor,"pizzas with",crustType,"crust costs","${:,.2f}".format(total) + ".")
print("\n----------------")