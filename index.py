import pandas as pd

# f = open('/Users/sergeyryabushko/Downloads/data_task4_old.txt', 'r')
#print(f.read())
#print(f.readline())

a_file = open("/Users/sergeyryabushko/Desktop/data_task4_old.txt")

number_of_lines = 500000

# for i in range(number_of_lines):
#     line = a_file.readline()
#     print(line)

x = 0

# for i in range(number_of_lines):
#     line = a_file.readline()
#     line_login = a_file.read(8)
#     x = x + 1
#     print(line)
#     print("accesor login:", line_login)
#     print(x)


users = []
x = 0

a = "login0	190561754.0	1.0	2017-04-20 12:10:30	2017-04-20 12:28:29"
b = a.split()
print(b)
print(b[0])
total_microtask = 0

for i in range(number_of_lines):
    line = a_file.readline()
    a = line.split()
    line_login = a[0]
    microtask = float(a[2])
    if users.count(line_login) == 0:
        users.append(line_login)
        users.append(total_microtask)
        total_microtask = 0
    else:
        total_microtask = total_microtask + microtask




print(len(users))
print(users[0:100])

