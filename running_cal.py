keeper = 0
quest = ""
undo = []

while True:
    operator = input(f"{quest}").strip().split()
    operand2 = 0
   
    if len(operator) == 3:
        operand,opera,operand2 = operator
        keeper = operand
    elif len(operator) == 2:
        opera,operand2 = operator
    elif len(operator) == 1:
        opera = operator[0]
    if keeper is list:
        keeper = "".join(keeper)
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
                if len(quest.split()) > 1:
                    keeper = undo.pop()
                    print(keeper)
                    quest = quest.split()
                
                    quest.pop()
                   
                    quest.pop()
                    
                    quest = " ".join(quest)
                else:
                    print("can not undo")
                
            else:
                print("nothing to undo")
                continue

    else:
        print("invalid operator")
