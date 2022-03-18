input_number = int(input('Enter the Value: '))
result_list = []
for x in range(1, input_number + 1):
    if input_number % x == 0:
        result_list.append(x)

print(result_list)

