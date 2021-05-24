# 1
def transform_data(fn):
    print(fn(10))

# 2
transform_data(lambda data: data / 5)

# 3
def transform_data2(fn, *args):
    for arg in args:
        print(fn(arg))

transform_data2(lambda data: data / 5, 10, 15, 22, 30)

# 4
def transform_data2(fn, *args):
    for arg in args:
        print('Result: {:^20.2f}'.format(fn(arg)))

transform_data2(lambda data: data / 5, 10, 15, 22, 30)