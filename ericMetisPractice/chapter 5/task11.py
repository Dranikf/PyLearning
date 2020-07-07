numbers = list(range(1,11))

for number in numbers:
    if number == 1:
        end = 'st';
    elif number == 2:
        end = 'nd';
    elif number == 3:
        end = 'rd';
    else:
        end = 'th';

    print(str(number) + end)
