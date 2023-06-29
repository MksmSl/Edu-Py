def pascal_triangle(row_index: int) -> list
    row_1 = 1
    triangle = [[1]]
    for i in range(1, row_index + 1): # create a rows
        
        for j in range(1, (len(1)+1)): # create elements in row
            row_i = 