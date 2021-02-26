try:
    import sys

    sum = 0
    for num in range(1, len(sys.argv)):
        print(sys.argv[num])
        sum += int(sys.argv[num])
    print("Ths sum is {}".format(sum))


except ZeroDivisionError:
    print("Zero division error occured")
    sys.exit(0)
except ImportError:
    print("Problem with import")
except KeyboardInterrupt:
    print("Some one used control+ c")
except Exception:
    print("Some problem")

"""

import sys
print(sys.argv)
print(type(sys.argv))

for i in sys.argv:
    print (i)
"""
