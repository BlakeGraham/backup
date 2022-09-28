var = int(input('please enter a number between 1 and 100'))

def square(var):
    if (var > 0 and var < 101):
        print('you entered: ' + str(var))
        print(type(var))
        print(str(var*var))
    else:
        print('number out of range')