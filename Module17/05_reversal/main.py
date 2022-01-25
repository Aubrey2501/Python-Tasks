string = input('\nВведите строку: ')
# string = 'hqwehrty'

begin = string.index('h')
end = string[begin + 1:].index('h')
result_string = string[end: begin: -1]
print('Развёрнутая последовательность между первым и последним h:', result_string)

# зачет!
