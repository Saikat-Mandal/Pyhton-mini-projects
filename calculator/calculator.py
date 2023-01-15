
def add(a , b):
    return a+b
def subtract(a , b):
    return a-b
def multiply(a , b):
    return a*b
def devide(a , b):
    return a/b


operations ={
    "+":add,
    "-":subtract,
    "/":devide,
    "*":multiply,
}    



def calculator():
    flag = True
    a = int(input("Enter the first number : \n"))
    for i in operations:
        print(i)
    while flag:        
        op = input("Enter an operation :\n")
        b = int(input("Enter the second number : \n"))

        calc = operations[op]
        ans = calc(a,b) 
        print(ans)
        print("\n")

        val = input("Press 'y' to continue or 'new' to start new calculation or 'n' to exit\n")
        if val == 'y':
            a = ans
        elif val =='new':
            calculator()   
        else:
            flag = False    
    

       
calculator()



