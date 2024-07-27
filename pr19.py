ip = int(input("Enter a number:"))

sum = 0
for i in range(1,ip+1):
    sum = sum + i/(i+1)
    
print ("Output is ",sum)