mylist = []
print("Enter four numbers")
for i in range(0,4):
  print("Enter number at index", i, )
  item = int(input())
  mylist.append(item)
print("List: ", mylist)

for item in mylist:
  print(item)

