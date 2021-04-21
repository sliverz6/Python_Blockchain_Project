# 과제 1
def func1(func):
    print(func(3))

# 과제 2
func1(lambda x: x+2)

# 과제 2
def func2(*args):
    for func in args:
        print(func(2))

func1(lambda x: x+2)

def transform_data(fn):
    print(fn(10))

transform_data(lambda data: data / 5)

def transform_data2(fn, *args):
    for arg in args:
        print(fn(arg))

transform_data2(lambda data: data / 5, 10, 15, 22, 30)

def transform_data3(fn, *args):
    for arg in args:
        print("Result: {:^20.2f}".format(fn(arg)))

transform_data3(lambda data: data / 5, 10, 15, 22, 30)