def fibonacci(n):
    pre_previous_number = 1
    previous_number = 1
    for i in range(1, n+1):
        if (i == 1):
            print(pre_previous_number)
        elif (i == 2):
            print(previous_number)
        else:
            current_number = pre_previous_number + previous_number
            pre_previous_number = previous_number
            previous_number = current_number
            print(current_number)

fibonacci(2)


            
    
