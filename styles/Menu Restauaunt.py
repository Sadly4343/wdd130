# Added an additional tab that includes a discount opportunity! Taking 25% off from the total cost and calculating it before final. 
#This adds an exciting way to fuel more purchases so the discount they can acheive.


def menu():
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute Total")
    print("5. Discount Opportunity!")
    print("5. Quit")
food_list = []
cost_list = []
index = [None]
menu()
option = int(input("Enter your option: "))
while option != 0:
    
    if option == 1:
        print("You would like to add item. ")
        print("1. Water for $7.99")
        print("2. Cereal for $5.99")
        print("3. Ocean for $4.99 ")
        add = int(input("Enter your option: " ))
        
        if add == 1:
            food_list.append("water")
            cost1 = float(input("What is the cost of Water?  "))
            cost_list.append(cost1)
        
        elif add == 2:
            food_list.append("cereal")
            cost1 = float(input("What is the cost of Cereal?  "))
            cost_list.append(cost1)
        
        elif add == 3:
            food_list.append("Ocean")
            cost1 = float(input("What is the cost of Ocean?" ))
            cost_list.append(cost1)
        else: 
            print("Invalid Choice Try Again")
        
    
    elif option == 2:
        print("You would like to view cart")
        for i in range(len(food_list)):
            food = food_list[i]
            cost = cost_list[i]
            i += 1
            print(f"{i}. {food} - ${cost}")
    
    elif option == 3:
        print("You would like to remove item")
        for i in range(len(food_list)):
            food = food_list[i]
            cost = cost_list[i]
            print(f"{i + 1}. {food} - ${cost}")

        print()
        
        index = int(input("Which item to change? ")) 
        if index > 0 and index <= len(food_list):
            deleted = food_list.pop(index - 1 )
            deleted_food = cost_list.pop(index - 1)
        else:
            print("Not correct length try again")
        
    elif option == 4:
        print("You would like to compute total")
        result = sum(cost_list)
        result_round = (round(result, 2))
        if result_round>=10:
            print("You have won a 25% discount")
            result_round *= 0.75
        else:
            print("You did not spend enough for the discount!")
        print(f"The total price of the items in the shopping cart is ${result_round}")

    elif option == 5:
        print("If you spend over $10 you will get a 25% discount!!!!!!")
    
    elif option == 6:
        break
      
    print()
    menu()
    option = int(input("Enter your option: "))
print("Thanks for using this program. Goodbye")