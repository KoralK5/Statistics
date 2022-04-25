from math import sqrt
from collections import Counter


def population(x):
    return len(x)


def variance(x):
    return sum((i - sum(x) / population(x)) ** 2 for i in x) / population(x)


def standard_deviation(x):
    return sqrt(variance(x))


def frequency(x):
    return Counter(x)


def mean(x):
    return sum(x) / population(x)


def median(x):
    return (
        x[population(x) // 2]
        if population(x) % 2 == 1
        else mean((x[population(x) // 2 - 1], x[population(x) // 2]))
    )


def mode(x):
    freqs = frequency(x)
    return freqs.most_common(1)[0][0]


def data_range(x):
    return max(x) - min(x)


def quartiles(x, q):
    x.sort()
    return [population(x) * (i / q) for i in range(1, q + 1)]


def quartile_split(x, q):
    qs = quartiles(x, q)
    print(qs)
    return [x[: int(qs[0])]] + [x[int(qs[i]) : int(qs[i + 1])] for i in range(q - 1)]


def class_width(x, i):
    return max(x[i]) - min(x[i])


def class_midpoint(x, i):
    return median(x[i])


def class_frequency(x, i):
    return sum(frequency(x[i]).values())


def class_mean(x):
    return sum(class_midpoint(x, i) for i in range(len(x))) / sum(
        class_frequency(x, i) for i in range(len(x))
    )
