def unlimited_arguments(*args, **keyword_args):
    print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, argument)


unlimited_arguments(1, 2, 3, 4, name="Jay", age=29)
