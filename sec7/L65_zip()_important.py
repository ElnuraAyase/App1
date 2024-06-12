docs = ['text.txt', 'book.txt', 'plan.txt']
todos = ['work must be done ', 'create folder', 'write poem']
for doc, todo in  zip(docs, todos):
  file = open(f"tasks/{doc}", 'w')
  file.write(todo)   
# it will write the tasks to your docs:text.txt, book.txt, paln.txt   if you stored them in the same directory in the folder file 


  # same logic, simplier to understand
letters = ['a', 'b', 'c']
todos = ['work must be done ', 'create folder', 'write poem']
x = zip(letters, todos) # be careful not letter or todo , but letters and todos as it must be name of the list not of the item
print(list(x))
