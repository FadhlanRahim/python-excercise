#its shit right now, can only do 2 by 2 matrices
#apparently, there is something called zip, and its actually the better way to loop over 2 lists
#dont hardcode

def add(matrix1, matrix2):
    combined = []
    for row1, row2 in zip(matrix1, matrix2):
        row = [n + m for n, m in zip(row1, row2)] # list comprehension
        #row = []                                   #these are not
        #for n, m in zip(row1, row2):
            #row.append(n + m)
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


#try addding 2 2x2 matrices to test the code
matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -3], [-4, 5]]
print(matrix1)
print(matrix2)
print(add(matrix1, matrix2))