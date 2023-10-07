numbers = input()

i = 0
while True:
    i += 1
    number = str(i)
    while len(number) > 0 and len(numbers) > 0:
        if number[0] == numbers[0]:
            numbers = numbers[1:]
        number = number[1:]
    if numbers == '':
        print(i)
        break
