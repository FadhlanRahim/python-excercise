#its shit right now, can only do 2 by 2 matrices
#apparently, there is something called zip, and its actually the better way to loop over 2 lists
#dont hardcode, do list comprehension

def add(matrix1, matrix2):
    combined = []
    for row1, row2 in zip(matrix1, matrix2):
        combined.append([n + m for n, m in zip(row1, row2)]) #these are list comprehension, could be reduced into just 1 line, but its harder to read
    return combined

#try addding 2 2x2 matrices to test the code
matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -3], [-4, 5]]
print(matrix1)
print(matrix2)
print(add(matrix1, matrix2))


#these are not list comprehension
        #row = []                                   
        #for n, m in zip(row1, row2):
            #row.append(n + m)