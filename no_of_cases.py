counter = {'Upper_case': 0,
        'Lower_case' :0}

string = input("Enter a string: \n")
for letter in string:
    if letter.isupper():
        counter['Upper_case'] += 1

    elif letter.islower():
        counter['Lower_case'] += 1

    else:
        pass

print(f'The original string was: {string}')

print(f'The number of upper case letters is {counter["Upper_case"]}')
print(f'The number of lower case letters is {counter["Lower_case"]}')
