n = int(input("Enter the length of the sequence: ")) 

a = 1
b = 2
c = 3
total = a+b+c
for i in range(0, n):
    if i == 0:
        print(1)
    if i == 1:
        print(2)
    if i == 2:
        print(3)
    
    if i >=3 :
        print(total)
        temp_total = total
        total = total+ b+c
        a =b
        b =c
        c = temp_total
 