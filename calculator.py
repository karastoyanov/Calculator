calc_operation = input("Enter the operation: \n [+] for addition \n [-] for substract \n [*] for multiply \n [/] for division \n")
a = float(input())
b = float(input())
result = 0

while True:
    
    if calc_operation == "+":
        result = a + b
        print(f"{result:.2f}")
    if calc_operation == "-":
        result = a - b
        print(f"{result:.2f}")
    if calc_operation == "*":
        result = a * b
        print(f"{result:.2f}")       
    if calc_operation == "/":
        result = a / b
        print(f"{result:.2f}")
        
        
    a = float(input())
    b = float(input())
    if a == "stop" or b == 'stop':
        break

print(f"{result:.2f}")
