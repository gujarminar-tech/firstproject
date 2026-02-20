def my_custom_decorator(func):
    def wrapper(*args, **kwargs): 

        arg_list=list(args)
        if len(args)<2:
            arg_list=arg_list+[1,2]
        first_num = arg_list[0]
        second_num = arg_list[1] 
        if not (isinstance(first_num, int) and isinstance(second_num,int)):
            raise ValueError("One of the input is not an integer ")
    
        args= tuple([first_num,second_num])

        kwargs.setdefault("d",0)
        kwargs.setdefault("e",0)

        return func(*args, **kwargs)
    return wrapper

@my_custom_decorator
def addition(a,b,**kwargs):
    d=kwargs["d"]
    e=kwargs["e"]
    c=a+b+d+e
    return c

print(addition(2,3,d=2))
print(addition(2,3.5))
