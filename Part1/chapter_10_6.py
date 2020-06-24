#Addition

while True:
    try:
        number = int(input('put some number'))
    except ValueError:
        print("you put wrong value[first number]")
        print("Pls try put again")

try:
    number_2=int(input('put some second number'))
except ValueError:
    print("you put wrong value[second number]")
result = number+number_2
print(result)