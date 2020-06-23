def str_convert(data):
    num = int(data)
    if num<10:
        return int(0), num
    else:
        return int(data[0]), int(data[1])

str_data = input()
init_data = int(str_data)
count = 0
while True:
    # 주어진숫자를 2개로 쪼갬
    a, b = str_convert(str_data)
    # 쪼갠 숫자를 더함
    sum_data = a+b
    # 더해진 숫자를 다시 쪼갬
    c, d = str_convert(str(sum_data))
    # b와 d를 더하여 str_data를 생성함
    str_data = str(b)+str(d)
    count += 1
    if init_data == int(str_data):
        break
print(count)
