file = open('any.txt', 'w')
file.write('hello he is the text for this code \n where you can see the difference') # for reading simple string

file.writelines(['line1\n,', [line2\n]] # for reading the list
file.close()

file.readlines()
              # output is a list with multiple string objects
file.read()
                # outpus is jsut a plane text
