def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
         print(f"{k}:{v}")
fun(first_name="yogesh",last_name="kumawat")

