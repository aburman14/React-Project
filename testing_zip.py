# importing required modules
import zipfile
import os



dirame='C:\\Users\\Ankita Burman\\Desktop\\Work\\python\\ZIP_check'
files=os.listdir(dirame)
# print(files)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

filepath=[]
for file_name in files:
    fullfilepath = os.path.join(dirame,file_name)
    filepath.append(fullfilepath)

# print(filepath)
  
# with ZipFile('my_python_files.zip','w') as zip:
#     # writing each file one by one
#     for file in files:
#         zip.write(file)   
  

fullpath=f'{dirame}\\files.zip'
print(fullpath)


myzip=zipfile.ZipFile(f'{dirame}\\files.zip','w')
print(myzip)
for nm in files:
    print(nm)
    myzip.write(nm)



os.remove('test1.txt')



##adding to check versions


####more versions