from re import search


regexp = r'^\+?(38)?8?[- (]?0\d{2}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}$'
phone_numbers = ['+38(096)567-86-67',
                 '+38(096)5678667',
                 '+380965678667',
                 '380965678667',
                 '80965678667',
                 '0965678667',
                 '096-567-86-67',
                 '096 567 86 67',
                 '426345r6345',
                 '38426345r6345',
                 '+38(096)567-86-674']

for number in phone_numbers:
    result = search(regexp, number)

    if result is None:
        print(f'Invalid: {number}')
    else:
        print(f'Positive number: {result.group()}')