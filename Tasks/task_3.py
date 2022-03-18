
def fizz_buzz(input_list):
    for number in input_list:
        if number % 3 == 0 and number % 5 == 0:
            print('Fizz Buzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print('Nope')

def fizz_buzz2(input_list):
    for number in input_list:
        output_string = ''
        if number % 3 == 0:
            output_string += 'Fizz'
        if number % 5 == 0:
            output_string += ' Buzz' if output_string != '' else 'Buzz'
        output_string = 'Nope' if output_string == '' else output_string
        print(output_string)
        
       
given_list = [1, 9, 10, 15, 20, 30, 60]
fizz_buzz2(given_list)
