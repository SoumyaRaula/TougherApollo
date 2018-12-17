array = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

for rows in array:
    print (rows)

row_val = len(array[0])
col_val = len(array)

print (row_val, col_val)

max_hourglass = (row_val-2)*(col_val-2)
print(max_hourglass)
list_sum = []
sum = 0
for i in range(row_val-2):
    for j in range(col_val-2):
        sum = (array[i][j] + array[i][j+1] + array[i][j+2] + \
               array[i+1][j+1]+ \
               array[i+2][j]+ array[i+2][j+1]+array[i+2][j+2])
        
        list_sum.append(sum)
        sum = 0

print(list_sum)
print(max(list_sum))
