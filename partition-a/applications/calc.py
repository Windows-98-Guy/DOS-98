while True:
    a = input('Number I: ')
    b = input('Operator: ')
    c = input('Number II: ')

    if '+' in b:
        print(f'Answer: {float(a) + float(c)}')
        print()
    elif '-' in b:
        print(f'Answer: {float(a) - float(c)}')
        print()
    elif '*' or 'x' in b:
        print(f'Answer: {float(a) * float(c)}')
        print()
    elif '/' or ':' in b:
        print(f'Answer: {float(a) / float(c)}')
        print()