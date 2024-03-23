list=[1,"sai",3.14,"karthik","surya","sai"]
list.append("sai kiran")
print(list)
list.insert(3,7)
print(list)
print(list[0])
print(list[1])
print(list[3])
for i in range(0,len(list)):
    print(list[i])
for i in list:
    print(i)
print(list[0:5])
print(list[1:4:2])
print(list[::2])
list[4]="ram"
print(list)