def factorial(x : int):
    fact = 1
    for i in range(1, x + 1):
        fact = fact * i
    return fact
        
if __name__ == "__main__":
    x = int(input("x : "))
    print(f"x! = {factorial(x)}")
