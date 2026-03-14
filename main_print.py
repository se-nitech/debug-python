def myfunc(x, y):
    z = 2 * x - y
    return z


def main():
    a = [1, 2, 3, 4, 5]
    b = None
    c = None

    print("c=%d, a1=%d, a5=%d" % (c, a[1], a[5]))
    c = a[1] + a[5]
    print("c=%d, a1=%d, a5=%d" % (c, a[1], a[5]))

    print("b=%d, c=%d, a1=%d" % (b, c, a[1]))
    b = c + a[1]
    print("b=%d, c=%d, a1=%d" % (b, c, a[1]))

    b = myfunc(b, c)

    print("b=%d" % b)


if __name__ == "__main__":
    main()
