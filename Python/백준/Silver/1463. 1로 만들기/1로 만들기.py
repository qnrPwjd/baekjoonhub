def to_one(num):
    for i in range(2, num + 1):
        to_1_count[i] = to_1_count[i - 1] + 1

        if i % 2 == 0:
            to_1_count[i] = min(to_1_count[i], to_1_count[i // 2] + 1)

        if i % 3 == 0:
            to_1_count[i] = min(to_1_count[i], to_1_count[i // 3] + 1)

    return to_1_count[num]

n = int(input())

to_1_count = [0] * (n + 1)

print(to_one(n))