def nod(num1, num2): 
    if(num2 == 0):
        return num1
    else: 
        return nod(num2, num1 % num2)