import os.path

count = input("Enter a string or a file path: ")
if os.path.isfile(count):
    words = count_words(None,count)
    print("The number of words in the file are: ", words)
else:
    words = count_words(count,None)
    print("The number of words in the string are: ", words)

