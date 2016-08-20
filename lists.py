start_list = [1, 2, 3, 4, 5]
square_list = []

for item_start in start_list:
    square_list.append(item_start ** 2)

square_list.sort()

for item_square in square_list:
    print(item_square)
