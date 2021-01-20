total_columns = 15
total_rows = 5
letters = [['-'] * total_columns for _ in range(total_rows)]


for row in range(total_rows):
    word = list(input())
    for idx, letter in enumerate(word):
        letters[row][idx] = letter

for col in range(total_columns):
    for row in range(total_rows):
        if letters[row][col] == '-':
            continue
        else:
            print(letters[row][col], end = '')