def myfunc(x, y):
    z = 2 * x - y
    return z


def main():
    a = [1, 2, 3, 4, 5]

    c = a[1] + a[5]
    b = c + a[1]
    b = myfunc(b, c)

    print(f"b={b}")


if __name__ == "__main__":
    main()
