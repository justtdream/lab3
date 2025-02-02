def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def filter_prime(inputList):
    resList = []
    for n in inputList:
        if is_prime(int(n)):
            resList.append(n)
    return resList

listIn = list(input("Enter numbers: ").split())
print("Prime numbers: ")
for n in filter_prime(listIn):
    print(n)

