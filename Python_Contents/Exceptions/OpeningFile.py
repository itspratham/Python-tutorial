import os
try:
    with open("data3.txt", encoding='utf-8') as fileobj:
        for line in fileobj:
            print(line)
except FileNotFoundError as ex:
    os.system('copy data.txt data3.txt')
    print("File not found!")
    print("Data.txt coppied to data3.txt")
except Exception as ex:
    print(ex)
else:
    print("No exception caused")
finally:
    print("Program executed.")