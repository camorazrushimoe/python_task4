a_file = open("/Users/sergeyryabushko/Downloads/data_task3.csv")

fname = ("/Users/sergeyryabushko/Downloads/data_task3.csv")
lines = 0
words = 0
letters = 0

for line in open(fname):
    lines += 1
    letters += len(line)

    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'

print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)

number_of_lines = 250001
assessors_stat = { }

for i in range(number_of_lines):
    line = a_file.readline()
    a = line.split()
    assessor_id = a[1]
    jud = a[3]
    cjud = a[4]
    if assessors_stat.get(assessor_id) == None:
        assessors_stat[assessor_id] = int(0)
    if jud != cjud:
        mistake_count = int(1)
        assessors_stat[assessor_id] = assessors_stat[assessor_id] + mistake_count

print(len(assessors_stat))

print(assessors_stat['1'])

print("result:")
for key, value in assessors_stat.items():
    print(key, value)