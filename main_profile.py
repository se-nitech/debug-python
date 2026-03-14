from line_profiler import profile

SIZE = 2026
REPEAT = 20


@profile
def sum_array(a, size):
    total = 0
    for i in range(size):
        total += a[i]
    return total


@profile
def average(a, size):
    return sum_array(a, size) // size  # 整数除算


@profile
def count_above_average(a, size):
    count = 0
    for i in range(size):
        if a[i] > average(a, size):
            count += 1
    return count


@profile
def count_above_average_fast(a, size):
    count = 0
    avg = average(a, size)
    for i in range(size):
        if a[i] > avg:
            count += 1
    return count


@profile
def main():
    a = [0] * SIZE
    total = 0

    for i in range(SIZE):
        a[i] = (i * 17) % 100  # 規則的な値で配列を初期化

    # 平均より大きい要素の数を数える（遅いバージョン）
    for i in range(REPEAT):
        total += count_above_average(a, SIZE)

    print("total={}".format(total // REPEAT))

    # 平均より大きい要素の数を数える（高速バージョン）
    total = 0
    for i in range(REPEAT):
        total += count_above_average_fast(a, SIZE)

    print("total={}".format(total // REPEAT))


if __name__ == "__main__":
    main()
