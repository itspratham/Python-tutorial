# import argparse
# parser = argparse.ArgumentParser(description="A simple argument parser", \
# epilog="This is where you might put example usage")
# parser.print_help()


# Args and Kwargs


def function(*args, **kwargs):
    # print("a
    print(args[0])
    print(args)
    print(kwargs)


# args = ("ram", "laxman", "Sita", "vdfjn", "nhn")

function(*("ram", "laxman", "Sita", "vdfjn", "nhn"))
#
# kwargs = {"ram": "1", "laxman": "2", "Sita": "3", "vdfjn": "4"}
#
#
# def function(ram, laxman, Sita, vdfjn):
#     print("args1:", ram)
#     print("args2: ", laxman)
#     print("arg3:", Sita)
#     print("Args4: ", vdfjn)
#     # print(kwargs)
#
#
# function(**kwargs)
