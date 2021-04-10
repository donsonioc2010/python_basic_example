print("Hello Wrold!")

for b in range(1, 1001):
    for a in range(0, b):
        c = 1000 - a - b
        print("a={}".format(a))
        print("b={}".format(b))
        print("c={}".format(c))

        if c <= a or c <= b or b <= a:
            break
        if (a * a) + (b * b) == (c * c):
            print(a * b * c)