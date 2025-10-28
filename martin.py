import random

def table(a, b, c, d, e):
    print("x\t H(x)\tRem\tBin\tTrailingZeros")
    for i in range(len(a)):
        print(f"{a[i]}\t{b[i]}\t{c[i]}\t{d[i]}\t{e[i]}")

def hash_function(x):
    return (6 * x + 1)

def rem(x):
    return (x % 5)

def binary(x):
    return bin(32 + x)[3:]

def trailing_zero(x):
    if x == 0:
        return 0
    count = 0
    while (x & 1) == 0:
        count += 1
        x >>= 1
    return count

def flajolet_martin(dataset):
    h_x, re, Binary, r_a = [], [], [], []

    for x in dataset:
        h_val = hash_function(x)
        r_val = rem(h_val)
        b_val = binary(r_val)
        t_val = trailing_zero(r_val)

        h_x.append(h_val)
        re.append(r_val)
        Binary.append(b_val)
        r_a.append(t_val)

    table(dataset, h_x, re, Binary, r_a)
    print(f"\nEstimated number of distinct elements: {2 ** max(r_a)}")

dataset = [3, 4, 5, 3, 4, 3, 2, 3, 3]
flajolet_martin(dataset)
