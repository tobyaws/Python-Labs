import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
num1 = int(input("Choose a number: "))
method = ops[input("Choose a operation(add ( + ), subtract( - ), multiply( * ), divide( / ):")]
num2 = int(input("Choose another number: "))
ans = method(num1, num2)
print("Answer is ", ans)