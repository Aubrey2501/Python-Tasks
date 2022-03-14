zen_file = open('zen.txt', 'r')
zen_lst = zen_file.read().split('\n')
zen_file.close()
outp_lst = [zen_lst[i] for i in range(len(zen_lst) - 1, -1, -1)]
print()
for i_elem in outp_lst:
    print(i_elem)