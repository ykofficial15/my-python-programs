from tkinter.font import names


def fun(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

names=['yogesh','kumawat']
print(fun(names))