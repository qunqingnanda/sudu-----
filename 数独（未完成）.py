import random
import xlwt
import xlsxwriter
import xlrd
N=int(input("N:"))
H=int(input("H:"))
o=input("txt_or_xlsx:")
def generate_sudoku(N, H, o):
    matrix = [[0 for i in range(N)] for j in range(N)]
    num_list = [i for i in range(1, N+1)]
    random.shuffle(num_list)
    for i in range(N):
        for j in range(N):
            matrix[i][j] = num_list[(i + j) % N]
    for i in range(H):
        x = random.randint(0, N - 1)
        y = random.randint(0, N - 1)
        matrix[x][y] = 0
    # Output the sudoku
    if o == 'txt':
        with open('sudoku.txt', 'w') as f:
            for row in matrix:
                for col in row:
                    f.write(str(col) + ' ')
                f.write('\n')
    elif o == 'xlsx':
        workbook = xlsxwriter.Workbook('sudoku.xlsx')
        worksheet = workbook.add_worksheet()
        for i in range(N):
            for j in range(N):
                worksheet.write(i, j, matrix[i][j])
        workbook.close()
# Read the sudoku from file
def read_sudoku(filename):
    matrix = []
    if filename.endswith('.txt'):
        with open(filename, 'r') as f:
            for line in f:
                row = [int(num) for num in line.split()]
                matrix.append(row)
    elif filename.endswith('.xlsx'):
        workbook = xlrd.open_workbook(filename)
        worksheet = workbook.sheet_by_index(0)
        for row in range(worksheet.nrows):
            matrix.append(worksheet.row_values(row))
    return matrix
# Solve Sudoku
def solve_sudoku(matrix):
    # Find the empty cell
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row = i
                col = j
                break
    # Check if the sudoku is solved
    if row == -1 and col == -1:
        return True
    # Try to fill the empty cell
    for num in range(1, len(matrix)+1):
        if is_valid(matrix, row, col, num):
            matrix[row][col] = num
            if solve_sudoku(matrix):
                return True
            matrix[row][col] = 0
    return False
# Check if the number is valid
def is_valid(matrix, row, col, num):
    # Check the row
    for i in range(len(matrix)):
        if matrix[row][i] == num:
            return False
    # Check the column
    for i in range(len(matrix)):
        if matrix[i][col] == num:
            return False
    # Check the small box
    box_row = row - row % N**0.5
    box_col = col - col % N**0.5
    for i in range(int(box_row), int(box_row+N**0.5)):
        for j in range(int(box_col), int(box_col+N**0.5)):
            if matrix[i][j] == num:
                return False
    return True


#生成一个数独
generate_sudoku(N, H, o)