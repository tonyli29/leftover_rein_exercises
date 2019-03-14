array = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

free = 0

for num in range(0, len(array)):
    for num2 in range(0, len(array[num])):
        if array[num][num2] is None:
            print(("Row {} seat {} is empty.".format(num+1, num2+1)))
            print(f'Would you like to site in row {num+1} seat {num2+1}')

            x = input()
            if x == 'y':
                print('what is your name?')
                y = input()
                array[num][num2] = y
                print(array)
                break
            if x == 'n':
                continue
            break
