# к тестовому заданию
def sequence():
    num = 1
    count = 1
    while True:
        yield num
        if count == num:
            num += 1
            count = 0
        count += 1


gen = sequence()
n = int(input('Введите число: '))

for i in range(n):
    print(next(gen), end=' ')
