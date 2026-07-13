x = int(input("Enter first number:   "))
oper = input("Enter Operator:   ")
y = int(input("Enter Second number:   "))

match oper:
    case '+':
        ans = x + y
    case '-':
        ans = x - y
    case '*':
        ans = x * y
    case '/':
        ans = x / y

print(ans)