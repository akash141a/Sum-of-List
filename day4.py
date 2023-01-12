list=[]
total=0
b = int(input("Enter the Limit of the List : "))
for i in range(b):
    c = int(input("Enter the Element : "))
    list.append(c)
    total+=c
print("List is = ",list)
print("Sum of List is : ",total)