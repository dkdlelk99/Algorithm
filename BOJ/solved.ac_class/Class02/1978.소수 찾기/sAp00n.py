from sys import stdin


def sieve_of_eratosthenes(Maximum):
    numbers = {}
    for number in range(2, Maximum + 1):
        numbers[number] = True
    root_of_max = int(Maximum ** 0.5)
    for i in range(2, root_of_max + 1):
        if numbers[i]:
            n = 2
        while i * n <= Maximum:
            numbers[i * n] = False
            n += 1
    return [j for j in range(2, Maximum + 1) if numbers[j]]


N = int(stdin.readline().strip('\n'))

list_of_numbers = list(map(int, stdin.readline().strip('\n').split()))
Maximum_number = max(list_of_numbers)
sieve = sieve_of_eratosthenes(Maximum_number)

print(
    len([ number for number in list_of_numbers if number in sieve])
)
