rows = 5  # Number of rows in the pyramid

for i in range(1, rows + 1):  # Loop from 1 to 5 (inclusive)
    print(" " * (rows - i) + "*" * (2 * i - 1))
