def open_write_close(Mystring):
    fo = open("C:\Test\Foo.txt", "a+") #see what the buffering parameter does

    fo.write(Mystring)

    fo.close()




Mystring = "Param1, Param2\n"

open_write_close(Mystring)
