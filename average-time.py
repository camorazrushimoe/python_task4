a_file = open("/Users/sergeyryabushko/Desktop/data_task4_old.txt")

number_of_lines = 701827

users = []
av_sec_for_microtask = []
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

    seconds_for_task = float(task_time) #Кол-во секунд на всю задачу
    sec_for_microtask = seconds_for_task / microtask #Кол-во секунд на микротаск в задаче
    av_sec_for_microtask.append(sec_for_microtask) #Складываем кол-во секунд по микротаску в массив

print("Кол-во заданий: ", len(av_sec_for_microtask))
av_sec_for_microtask.sort()
print(av_sec_for_microtask[100000:100010])




print("\n\n\n")

a = 0
sum = 0
min_time = 500
max_time = 0

while a < 701826:
    sum = sum + av_sec_for_microtask[a]
    a = a + 1
    actual_time = sum / a
    if actual_time < min_time:
        min_time = actual_time
    if actual_time > max_time:
        max_time = actual_time
    # if a != 0:
    #     print("Среднее время на микро таск:", sum / a)

print(sum)
print("Среднее время на микротаск:", sum / 701826)
print(min_time)
print(max_time)


