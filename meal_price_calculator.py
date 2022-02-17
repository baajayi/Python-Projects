#requesting input
name = input("What is your name? ")
meal_price_child = float(input("What is the meal price for a child? "))
meal_price_adult = float(input("What is the meal price for an adult? "))
bottle_of_drink = float(input("How much is a bottle of drink? "))
children_number = int(input("How many children are in the group? "))
adult_number = int(input("How many adults are in the group? "))
drinks_total = bottle_of_drink * (children_number + adult_number) #A bottle of drink for everyone
sales_tax_rate_in_percentage = float(input("Please enter the sales tax rate: "))
tip_rate_in_percentage = float(input("Please enter the tip rate: "))
#computing the subtotal and the tip
subtotal = (meal_price_child * children_number) + (meal_price_adult * adult_number) + drinks_total
tip = (tip_rate_in_percentage / 100) * subtotal
print() #Printing a blank line
#Displaying the subtotal
print(f"Subtotal = ${subtotal:.2f}")
#computing and displaying the sales tax
print(f"Sales tax = ${(sales_tax_rate_in_percentage / 100) * subtotal:.2f}")
#displaying the tip amount
print(f"Tip = ${tip:.2f}")
#Computing the total by adding the subtotal, sales tax and tip
total = subtotal + ((sales_tax_rate_in_percentage / 100) * subtotal) + (subtotal * (tip_rate_in_percentage / 100))
print() #another blank line
print(f"Total = ${total:.2f}")
#asking for the payment amount
payment = int(input("what is the payment amount in USD? "))
print()
#displaying the change
print(f"Change = ${payment - total:.2f}")
print()
print(f"***{name}, Thank you for eating with us, please visit again!***")