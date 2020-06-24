#Addition Calculator

while True:
    try:
        number = int(input('put first number'))
        break

    except ValueError:
        print("you put wrong value[first number]")
        print("Pls try put again")

while True:
    try:
        number_2 = int(input('put second number'))
        break

    except ValueError:
        print("you put wrong value[second number]")
        print("Pls try put again")

result = number+number_2
print(result)