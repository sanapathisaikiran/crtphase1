dic={1:"karthik",
     2:"saripoda sanivaram",
     3:"sai",
     143:"oG",
     "1":"pushpa"}
#mutable
dic[1]="devra"
print(dic)
#add new value pair
dic["143"]="kalki"
print(dic)
#access value
print(dic[2])
#using for loop
for i in dic:
    print(i)
for i in dic.values():
    print(i)
for i,j in dic.items():
    print(i,j)
dic.pop(3)
print(dic)