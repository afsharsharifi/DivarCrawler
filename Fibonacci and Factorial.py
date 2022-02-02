def Fibonachi(num):
    num0 = 0
    num1 = 1

    ListOfFibonachies = [num0, num1]

    for number in range(2, num+1):
        next_num = num0 + num1

        ListOfFibonachies.append(next_num)
        num0 = num1
        num1 = next_num
    return ListOfFibonachies[num]


def Factorial(num):
    I = 1
    S = 1

    while I < num+1:
        S = S * I
        I = I + 1
    return S


print(f"Fibonachi of 10 => {Fibonachi(10)}")
print(f"Factorial of 5 => {Factorial(5)}")
