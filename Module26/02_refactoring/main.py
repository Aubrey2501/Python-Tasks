# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break

def refactoring(lst1, lst2):
    for x in lst1:
        for y in lst2:
            result = x * y
            yield result


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
my_generator = refactoring(lst1=list_1, lst2=list_2)
if to_find in my_generator:
    print('Found!!!')
else:
    print('Not found')



