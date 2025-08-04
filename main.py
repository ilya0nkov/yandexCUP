s1 = str(input())
s2 = int(input())

mas = list(map(str, s1))
arr = []
for i in range(len(mas)):
    if mas[i] != " ":
        arr.append(int(mas[i]))
start = min(arr)
count = 0
for i in range(start, 10 ** 18 + 1):
    counter = 0
    for j in range(len(arr)):
        if i % arr[j] == 0:
            counter+=1
            if counter == 3:
                continue
    if counter != 2:
        continue
    count += 1
    if count == s2:
        print(i)
        break
    elif i == 10 ** 18 + 1:
        print(-1)