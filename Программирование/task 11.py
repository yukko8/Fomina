def simple():
    number = int(input("Введите число "))
    j = 0
    for i in range(1, number + 1):
        if number % i == 0:
            j+=1   
    if j <=2:
        print("Это простое число")
    if j > 2:
        print("Это не простое число")


if __name__ == "__main__":
    simple() 