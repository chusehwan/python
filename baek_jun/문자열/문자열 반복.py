iter = int(input())
text_list = []
print_result = ''

for i in range(iter):
    num_n_string = input()
    text_list.append(num_n_string)

for i in range(iter):
    cov_string = text_list[i].split()
    cov_num = int(cov_string[0])
    string = cov_string[1]
    len_of_string = len(string)
    for a in range(len_of_string):
        result = string[a] * cov_num
        print_result = print_result + result
    print(print_result)
    print_result = ''
    cov_string = None
    cov_num = None