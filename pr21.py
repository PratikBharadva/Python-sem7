ip = int(input("Enter a number:"))

#pattern 1:
'''for i in range(1,ip+1):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")
    print()
'''    
#pattern 2:
'''for i in range(1,ip+1):
    for space in range(ip-i,0,-1):
        print('',end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
for i in range(ip-1,0,-1):
    for space in range(ip-i,0,-1):
        print('',end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
'''    
#pattern 3:
for i in range(ip,0,-1):
    temp = ip-i+1
    for j in range(1,i+1):
        print(temp,end=" ")
    print()
