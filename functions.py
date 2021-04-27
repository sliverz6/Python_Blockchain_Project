def unlimited_arguments(*args, **kargs):
    print(args)
    print(kargs)


unlimited_arguments(name="Jay", age=29)

print(*[1, 2, 3, 4])
