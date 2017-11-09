global file_is_open
file_is_open = False

def write_in_file(path_of_file, stringToWrite):
    #add check if file is already open
    #if file_is_open == True:
        #return ('file already opened')
    
    file_is_open = True
    
    fo = open(path_of_file, "w") #Todo see what the buffering parameter does
    fo.write(Mystring)
    fo.close()
    
    file_is_open = False




def read_and_delete_from_file(path_of_file):
    #add check if file is already open
    #if file_is_open == True:
        #return ('file already opened')
    
    file_is_open = True
    
    fo = open(path_of_file, "r") #Todo see what the buffering parameter does
    File_string == fo.readline()
    print (File_string)
    fo.close()

    file_is_open = False


Mystring = "Param1, Param2\n"
MyPath = "C:\Test\Foo.txt"

write_in_file(MyPath, Mystring)
