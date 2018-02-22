

str1 = 'CTTAGA' # chuoi dai lam dong
str2 = 'GTAA' # chuoi ngan lam cot
str3 = str1 # k + dau - nhu string 1
str1 = '-' + str1
str2 = '-' + str2

rows = len(str1) + 1
cols = len(str2) + 1

matrix = [['0' for i in range(cols)] for j in range(rows)]

i = 1
while(i != rows):
  matrix[i][0] = str1[i - 1]
  i = i + 1

i = 1
while(i != cols):
  matrix[0][i] = str2[i - 1]
  i = i + 1

####################
i = 2
while(i != cols):
  matrix[1][i] = str(int(matrix[1][i - 1]) + -2)
  i = i + 1

i = 2
while(i != rows):
  matrix[i][1] = str(int(matrix[i - 1][1]) + -2)
  i = i + 1

#########################
i = 2
while(i != rows):
  j = 2
  while(j != cols):
    d = 1
    if matrix[i][0] != matrix[0][j]:
      d = -1
    matrix[i][j] = str(max(int(matrix[i - 1][j - 1]) + d, int(matrix[i - 1][j]) - 2, int(matrix[i][j - 1]) - 2))
    j = j + 1
  i = i + 1

###########################
arr_tb = []

def traceback(matrix, r, c, str_tb = str(rows - 1) + str(cols - 1) + '.'):
    if r == 1 and c == 1:
        
        arr_tb.append(str_tb)
        return

    d = -1
    if matrix[r][0] != matrix[0][c]:
        d = 1

    temp = int(matrix[r][c]) + 2
    temp_dia = int(matrix[r][c]) + d

    if matrix[r - 1][c - 1] == str(temp_dia):
        traceback(matrix, r - 1, c - 1, str_tb = str_tb + str(r - 1) + str(c - 1) + '.')

    if matrix[r - 1][c] == str(temp):
        traceback(matrix, r - 1, c, str_tb = str_tb + str(r - 1) + str(c) + '.')

    if matrix[r][c - 1] == str(temp):
        traceback(matrix, r, c - 1, str_tb = str_tb + str(r) + str(c - 1) + '.')

traceback(matrix, rows - 1, cols - 1)

arr_tb = [s.split('.') for s in arr_tb]

arr_tb = [[s for s in l if len(s) != 0]
          for l in arr_tb]

######################
str_des = []
for index in  range(len(arr_tb)):
    str_temp = ''
    for iter in range(len(arr_tb[index]) - 1):
        x1 = int(arr_tb[index][iter][0])
        y1 = int(arr_tb[index][iter][1])

        x2 = int(arr_tb[index][iter + 1][0])
        y2 = int(arr_tb[index][iter + 1][1])

        if x1 - 1 == x2 and y1 - 1 == y2:
            str_temp = str_temp + matrix[0][y1]
        else:
            str_temp = str_temp + '-'
    str_des.append(str_temp)

str_des = [s[::-1] for s in str_des]
####################
for i in matrix:
  print(i)

print('\n\n\n\n')

for j in arr_tb:
  print(j)

print('\n\n\n\n')

for j in str_des:
  print(str3 + '\n' + j + '\n--------')