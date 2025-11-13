list3=[5,9,2,7,12,4,6]
sum=0
for i in list3:
    sum=sum+i
print("The sum of the elements in the list", list3,"is",sum)
avg=sum/len(list3)
print("The average of the list", list3,"is",avg)
list3.sort()
print(list3)
print("The maximum number in the list is",list3[0])
print("The minimum number in the list is",list3[-1])