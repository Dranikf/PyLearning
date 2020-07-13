
while True:
    number1 = input('type some number: ');
    if number1 == 'q':
        break;
    number2 = input('type second number: ');
    if number2 == 'q':
        break;

    try:
        result = int(number1) + int(number2);
    except ValueError:
        print('no number entered');
    else:
        print('result is: ' + str(result));
