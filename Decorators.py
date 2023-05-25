def func1(fun):
    def wrapper():
        print("Hello")
        fun()
        print("Welcome to python")
    return wrapper
def func2():
    print("Code Academy")

f=func1(func2)
f()
