
import os
#test_file_write =  open("output.txt", "w+")
    #f1.write("Hi test data");
#test_file_write.write("test data write")

test_file_read = open("input.txt", "r")
#print (test_file_read.read().split('\n'))
print (test_file_read.read().upper())

#print (test_file_read.read().split('\r'))

#os.remove("output.txt")