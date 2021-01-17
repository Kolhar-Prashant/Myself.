
mat = [  ['3', '0', '6', '5', '0', '8', '4', '0', '0'],
         ['5', '2', '0', '0', '0', '0', '0', '0', '0'],
         ['0', '8', '7', '0', '0', '0', '0', '3', '1'],
         ['0', '0', '3', '0', '1', '0', '0', '8', '0'],
         ['9', '0', '0', '8', '6', '3', '0', '0', '5'],
         ['0', '5', '0', '0', '9', '0', '6', '0', '0'],
         ['1', '3', '0', '0', '0', '0', '2', '5', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '7', '4'],
         ['0', '0', '5', '2', '0', '6', '3', '0', '0']]


numbers = ['1','2','3','4','5','6','7','8','9']
'''
num_dict = {}  # will use for backtracking.
for num in range(82):
    num_dict[num]=[]'''

def check_vertically(col_num,digit):
    for row in range(3):
        if mat[row][col_num] == digit:
            return -1
    return 0

def check_horizontally(start_point,row_num,digit):
    for cell in range(start_point,3):
        if mat[row_num][cell] == digit:
            return -1
    return 0

def if_mat_complete():
    for row in mat:
        for cell in row:
            if cell == " ":
                return -1
    return 0

def print_matrix():
    for row in mat:
        print(row)

def solve():
    cell_no = 1
    for row in range(len(mat)):
        c_cell_no = 0
        for digit in mat[row]:
            if digit == "0":
                for temp_digit in numbers:
                    if temp_digit not in mat[row]:
                        if check_horizontally(c_cell_no,row,temp_digit) == 0:
                            if check_vertically(c_cell_no,temp_digit) == 0:
                                mat[row][c_cell_no] = temp_digit
                                c_cell_no=0
                                #num_dict[cell_no].append(temp_digit)
                                break
                    cell_no+=1
            c_cell_no+=1
    if if_mat_complete() == -1:
        solve()
    else:
        print_matrix()
solve()