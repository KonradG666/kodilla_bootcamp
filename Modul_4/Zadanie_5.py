def count_them_all(*args):
    positional_args_count = len(args)
    print(f"I have received {positional_args_count} positional arguments")

count_them_all(1, 2, 3, "A")
print("----------------------------------------------")
def count_them_all(*args, **kwargs):
    positional_args_count = len(args)
    kaywords_kwargs_count = len(kwargs)
    print(f"I have received {positional_args_count} positional arguments")
    print(f"I have received {kaywords_kwargs_count} kayworsd arguments")
count_them_all(1, 2, 3, "A", a = 1, b = 2)