
n = 1001
def even_odd(n, m):
    if n < 0:
        print(f'The Number {n} is negative')
    elif n % 2 == 0:
        print(f'The number {n} is Even')
    else:
        print(f'The number {n} is odd')
    return m

given_number = int(input('Enter the number: '))
output = even_odd(given_number, 1000)
print(output)
