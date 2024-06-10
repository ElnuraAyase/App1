myList = ['toy', 'aidan', 'iv', 'mouse']
newList = []
#show what is in the list already 
print(f"Initial items in my list: {myList}")

#pop method deletes an item from the list and assigns it to item

while myList:
    item = myList.pop(0)                                             
    special treat for one of the items in the list
    if item == aidan:
      newList.append(item.capitalize())
    else:
      newList.append(item) 
    
    print = (f"Item {item} is processing...")

    if item == 'aidan':
        print(f"Special item {item} is processing...")
      
    #show what is left in the mylist 
    print(f"Items remain in my list: {myList}")
#print confirmation
print("All items processed")
print("Processed new list: ", newList)   


'''
  if you put '0' in () like : .pop(0) then it will delete item index 0 and further ,
  if you leave it empty, like: .pop() it will delete from the last item in the list 
  
#output with .pop(0)
'''
  C:\Users\user\AppData\Local\Programs\Python\Python312\python.exe D:/python/petprojectsa/sec6/fstring_while_if_together.py
Initial items in my list: ['toy', 'aidan', 'life', '345']
Item toy is processing...
Items remain in my list: ['aidan', 'life', '345']
Item aidan is processing...
Special item aidan is processing...
Items remain in my list: ['life', '345']
Item life is processing...
Items remain in my list: ['345']
Item 345 is processing...
Items remain in my list: []
All items processed
Processed new list:  ['toy', 'Aidan', 'life', '345']

Process finished with exit code 0
'''
# output with .pop()
'''
C:\Users\user\AppData\Local\Programs\Python\Python312\python.exe D:/python/petprojectsa/sec6/fstring_while_if_together.py
Initial items in my list: ['toy', 'aidan', 'life', '345']
Item 345 is processing...
Items remain in my list: ['toy', 'aidan', 'life']
Item life is processing...
Items remain in my list: ['toy', 'aidan']
Item aidan is processing...
Special item aidan is processing...
Items remain in my list: ['toy']
Item toy is processing...
Items remain in my list: []
All items processed
Processed new list:  ['345', 'life', 'Aidan', 'toy']

Process finished with exit code 0

'''
