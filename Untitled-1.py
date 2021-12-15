import os 

path = r'C:\Users\Administrator\Desktop\新建文件夹 (2)'
bookpath = []
for root, dir, files in os.walk(path):
    print(root)
    print("****************")
    print(dir)
    print("////////////////")
    print(files)
    for filespath in files:
        s = os.path.join(root, filespath)
        print(s)
        bookpath.append(s)
    print("-------------")
print(len(bookpath))
