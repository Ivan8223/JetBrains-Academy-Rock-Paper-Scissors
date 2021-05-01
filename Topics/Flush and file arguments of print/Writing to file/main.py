f_name = "test.txt"
my_string = "A string to be written to a file!"

# what to do with the file and the string
with open(f_name, 'w') as file_:
    print(my_string, file=file_)
