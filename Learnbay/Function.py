def outer_fun():
    message = 'Local'

    def inner_fun():
        nonlocal message
        message = 'nolocal'
        print('inner message',message)
        inner_fun()
        print('Outer message',message)
    
outer_fun()



message = "outer-variable"

# outside function 
def outer():
    message = 'local'
    print("inner:", message)
    
    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner $$$$:", message)

    inner()
    print("outer:", message)

outer()
print("outside the outer_func", message)

c = 1
def add():

    global c 
    
    c= c + 1
    
    print (c)   

add()





    
