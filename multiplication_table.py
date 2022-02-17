a = int(input("How many rows and columns do you want? "))
x = 0
spaces = 0
print("Here's your multiplication table")
while x < a+1:
    for i in range(1, a+1):
        for x in range(1, a+1):
            product = x*i
            spaces = len(str(product))
            if x < a:
                if spaces <= 3:
                    print(f"{product:3}", end=" ")
                else:
                    print(f"{product:{spaces}}", end=" ")                        
            else:
                if spaces <= 3:
                    print(f"{product:3}")
                else:    
                    print(f"{product:{spaces}}")
    break
