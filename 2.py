s = str(input())

def count_steps(string):
    count_r = 0
    count_l = 0
    count_n = 0
    for i in string:
        if i == "R":
            count_r += 1
        elif i == "L":
            count_l += 1
        elif i == "?":
            count_n += 1
    return count_r, count_l, count_n


if __name__ == "__main__":
    max_len = 1
    count_r, count_l, count_n = count_steps(s)

    div = abs(count_r - count_l)
    if (count_l == 0 and count_r == 0 and count_n == 0):
        max_len = 1
    elif (count_r == 0 and count_l == 0):
        max_len = count_n
    elif (count_r == 0 or count_l == 0):
        max_len += div + count_n
    else:
        max_len += div + count_n

    if count_l > count_r:
        s.replace("?", "L")
    elif count_r > count_l:
        s.replace("?", "R")

    print(max_len)