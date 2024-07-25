filemanes= ["a", "b", "c"]
for filename in filenames:
  file = open(filename, 'r')
  content = file.read()
  print(content)
