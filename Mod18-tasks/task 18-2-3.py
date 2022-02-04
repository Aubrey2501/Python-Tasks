import random
ip_list = []
ip_adress = 'IP-адрес: {0}.{1}.{2}.{3}'

ip_list = [[random.randint(0, 255) for ipn in range(4)] for ip_ad in range(5)]
print(ip_list)

for ip in ip_list:
    ip_adr = ip_adress.format(ip[0], ip[1], ip[2], ip[3])
    print(ip_adr)