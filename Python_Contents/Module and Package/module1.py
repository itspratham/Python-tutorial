from xml.dom.minidom import *

try:
    import sys

    print(sys.argv)
    print(type(sys.argv))
    d = int(sys.argv[1])
    a = int(sys.argv[2])
    print("d is {} and a={} ans is {}".format(d, a, d / a))

except ZeroDivisionError:
    print("Zero division error occured")
    sys.exit(0)
except ImportError:
    print("Problem with import")
except KeyboardInterrupt:
    print("Some one used control+ c")
except Exception:
    print("Some problem")
