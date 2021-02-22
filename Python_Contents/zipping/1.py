# from zipfile import ZipFile
#
# # specifying the zip file name
# file_name = "my_python_files.zip"
#
# # opening the zip file in READ mode
# with ZipFile("hello.zip", 'w') as zip:
#     # printing all the contents of the zip file
#     zip.printdir()
#
#     # extracting all the files
#     print('Extracting all the files now...')
#     zip.extractall()
#     print('Done!')



import tempfile

#
#
#



first_name = ['Joe','Earnst','Thomas','Martin','Charles']
last_name = ['Schmoe','Ehlmann','Fischer','Walter','Rogan','Green']

# f = []
# for i in range(len(first_name)):
#     f.append((first_name[i], last_name[i]))
# print(f)

# f = list(zip(first_name,last_name))
# print(f)


print(tempfile.gettempdir())  # prints the current temporary directory

f = tempfile.TemporaryFile()
f.write('something on temporaryfile')
f.seek(0)  # return to beginning of file
print(f.read())  # reads data back from the file
f.close()  # temporary file is automatically deleted here
