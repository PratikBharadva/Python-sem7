#Transpose a Matrix
arr=[]
def getmatrix(row,col):

    for i in range(row):
        arr.append([])
        for j in range(col):
            arr[i].append(int(input("Enter a element:")))
    return arr

def transpose(arr,row,col):
    arr2 = []
    for j in range(col):
        arr2.append([])
        for i in range(row):
            arr2[j].append(arr[j][i])
    return arr2

row = int(input("Enter a number of row:"))
col = int(input("Enter a number of column:"))
arr = getmatrix(row,col)

newarr = transpose(arr,row,col)
print("Transpose of Matrix:")
print(newarr)