lines = 5

for i in range(1, lines + 1):
    spaces = " " * (lines - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
