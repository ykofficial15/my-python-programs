def outer_func():
    def inner_func():
        print("inside inner functiion")
    return inner_func

var=outer_func()
var()



def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2

var2=outer_func2("hello and welcome to the kapil sharma show")
var2()
