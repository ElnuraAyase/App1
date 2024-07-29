filemanes= ["a", "b", "c"] #all the texts as files in the list
for filename in filenames:
  file = open(filename, 'r')
  content = file.read()
  print(content)
