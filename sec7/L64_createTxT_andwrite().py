
# Use Python to create a file with name file.txt and write the text snail there.

with open("file.txt", 'w') as file: #'with' statement ensures that the file is properly closed after writing
    file.write("snail")
