x = 1
total_saved = 0
for i in range(52):
    total_saved += x
    x = x * 2
    print(str(x) + ' dollars in week:' + str(i))
    print('total so far: ' + str(total_saved))

