lst=['apple', 'banana', 'kivi', 'mango', 'guava']
print("Length of List: ",len(lst))
print("First Element:",lst[0])
print("Last Number:",[-1])
lst.append('papaya')
print("Updated List:",lst)
  #adding value in list
lst.remove('guava') 
print("Updated List:",lst)
#remove value 
lst.sort()
print("Sorted list:", lst)
#for sorting
lst.pop(1)
print("Updated List:",lst)
#for
lst.reverse()
print("Reversed List:",lst)
print("Sliced list:",lst*2)
lst=lst[:4]
print("Sliced List:",lst)
lst.clear()
print("Updated List:",lst)