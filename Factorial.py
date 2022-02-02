def Factorial(num):
    I = 1
    S = 1

    while I < num+1:
        S = S * I
        I = I + 1
    return S


print(f"Factorial of 5 => {Factorial(5)}")
