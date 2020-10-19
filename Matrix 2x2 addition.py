#its shit right now, can only do 2 by 2 matrices
#apparently, there is something called zip, and its actually the better way to loop over 2 lists

def add(matrix1, matrix2):
    combined = []
    for rows in zip(matrix1, matrix2):
        row = []
        for items in zip(rows[0], rows[1]):
            row.append(items[0] + items[1])
        combined.append(row)
    return combined

#def add(matrix1, matrix2):
#    combined = []
#    for i in range(len(matrix1)):
#        row = []
#        for j in range(len(matrix1[i])):
#            row.append(matrix1[i][j] + matrix2[i][j])
#        combined.append(row)
#    return combined