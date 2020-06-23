a = int(input())
# 토탈 별수 = a
iter_num  = a*2-1
st_num = iter_num
v_num = 0

for i in range(iter_num):
    vacant = ' '*v_num
    star = '*'*st_num
    p = vacant+star
    print(p)
    # 입력받은 수치만큼 별표 줄이기
    if i < a-1:
        st_num -=2
        v_num += 1

    else:
        st_num +=2
        v_num -= 1





