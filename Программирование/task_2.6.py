letter = input('Введите литеру ряда ').lower()
digit = int(input('Введите номер ряда '))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
digits = [1, 2, 3, 4, 5, 6, 7, 8]

letter_index = letters.index(letter)
digit_index = digits.index(digit)
if letter_index % 2 == digit_index % 2:
    print(' ─=≡Σʕっ•ᴥ•ʔっ Чёрная')
else:
    print('༼ ʘ‿ʘ༽ Белая')
