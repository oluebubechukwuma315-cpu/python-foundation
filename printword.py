# def delivery_cost(price,quantity,delivery):
#      total = write the item_cost(price, quantity) add it to the delivery
#      return total
# def item_cost(price, quantity):
#     solve the cost of the item 
#     then return the cost
# # what the question is asking from u is to just find total of a product by multiplying the price by the quantity and returning it 
# # then call the item_cost function in the delivery_cost then add the delivery fee to it
# operator = input("enter operator then num").strip().split()
# opera = 0
# if len(operator)  > 1:
#     operator, opera = operator
# else:
#     operator = "".join(operator)
# print(operator, opera)
# input(f"{operator}")

keeper = 0
quest = ""
undo = ["+"]

while True:
    operator = input(f"{quest}").strip().split()
    operand2 = 0
   
    if len(operator) == 3:
        operand,opera,operand2 = operator
        keeper = operand
    elif len(operator) == 2:
        opera,operand2 = operator
    elif len(operator) == 1:
        opera = operator
    if keeper is list:
        keeper = "".join(keeper)
    opera = "".join(opera)
    if operand2 is list:
        operand2 = "".join(operand2)
    try:
        keeper = float(keeper)
        operand2 = float(operand2)
    except ValueError:
        print("improper input format")
        continue
    if len(operator) == 3:
        quest += str(keeper)  + " "  + str(opera) + " " + str(operand2)
    if  len(operator) == 2 :
        quest +=  " " + str(opera)  + " " + str(operand2)
    if opera in ["+","-","/","*", "undo"]:
        if opera == "+":
            undo.append(keeper)
            keeper += operand2
            print(keeper)
        elif opera == "-":
            undo.append(keeper)
            keeper -= operand2
            print(keeper)
        elif opera == "/":
            undo.append(keeper)
            keeper /= operand2
            print(keeper)
        elif opera == "*":
            undo.append(keeper)
            keeper *= operand2
            print(keeper)
        elif opera == "undo":
            if undo :
                keeper = undo.pop()
                print(keeper)
                quest = quest.split()
                quest.pop()
                print(quest)
                quest.pop()
                print(quest)
                quest = "".join(quest)
                continue
            else:
                "nothing to undo"
                continue

    else:
        print("invalid operator")