a_file = open("/Users/sergeyryabushko/Desktop/data_task4_old.txt")

number_of_lines = 5000

users = []
x = 1

a = "login0	190561754.0	1.0	2017-04-20 12:10:30	2017-04-20 12:28:29"
b = a.split()
print(b)
print(b[0])
total_microtask = 0
user_number = float(0)
same_date = 0

for i in range(number_of_lines):
    line = a_file.readline()
    a = line.split()
    line_login = a[0]
    microtask = float(a[2])
    date_1 = a[3]
    time_1 = a[4]
    date_2 = a[5]
    time_2 = a[6]
    if date_1 != date_2:
        same_date = same_date + 1
        # print(line_login, time_1, time_2)
        task_time = 0
    else:
        # time 1
        hour1 = int(time_1[0:2])
        min1 = int(time_1[3:5])
        sec1 = int(time_1[6:8])

        # time 2
        hour2 = int(time_2[0:2])
        min2 = int(time_2[3:5])
        sec2 = int(time_2[6:8])

        task_hour = hour2 - hour1
        task_min = min2 - min1
        task_sec = sec2 - sec2

        task_time = task_sec

        if task_hour != 0:
            task_time = task_time + (task_hour * 60 * 60)
        if task_min != 0:
            task_time = task_time + (task_min * 60)

        # print("Sec:", task_time)

    seconds_for_task = task_time

    if users.count(line_login) == 0:
        users.append(line_login)
        users.append(total_microtask)
        total_microtask = 0
    else:
        total_microtask = total_microtask + microtask

# добавляем текущий тотал микро таск к последней цифре в массиве
    x = x + 1

print("Колическов строк:", x)
print("Кол-во юзеров:", len(users)/2)
print(users[0:100])
print("День назначения не совпадает с днем выполнения раз", same_date)
