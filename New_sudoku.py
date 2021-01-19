mat = [['1','0','3'],
       ['0','0','0'],
       ['0','1','0']]

org_mat = [['1','0','3'],
       ['0','0','0'],
       ['0','1','0']]

numbers = ['1','2','3']#,'4','5','6','7','8','9']

def col_check(col_num,num):
    for row in range(3):
        if mat[row][col_num] == num:
            return -1
    return 0

def is_complete(new_mat):
    for row in new_mat:
        for cell in row:
            if cell == '0':
                return -1
    return 0

def reset_row(row_num):
    temp_list = org_mat[row_num]
    row_indx = 0
    for _ in range(len(mat)):
        if row_indx == row_num:
            col=0
            for numbers in temp_list:
                mat[row_indx][col] = numbers
                col += 1
            break
        row_indx += 1

def solve(new_mat):
    row_indx = 0
    for row in new_mat:
        col_indx = 0
        for cell in row:
            if cell == '0':
                for num in numbers:
                    if num in row:
                        continue
                    else:
                        if col_check(col_indx,num) == 0:
                            mat[row_indx][col_indx] = num
                            break
                        else:
                            reset_row(row_indx)
                            continue
            col_indx += 1
        row_indx += 1
    if is_complete(new_mat) == -1:
        solve(new_mat)
    else:
        for row in mat:
            print(row)
        print("---")
solve(mat)