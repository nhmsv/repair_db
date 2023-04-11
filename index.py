import os
import shutil
from datetime import datetime
print("START")

parent_dir = "C:\\xampp\\mysql"
directory = "data_new"

# Path
path = os.path.join(parent_dir, directory)
ibdata1 = os.path.join(parent_dir+"\\data\\", "ibdata1")

source_folder  = parent_dir + "\\backup\\"
destination_folder  = parent_dir + "\\new_data\\"

def copyDataDirs():
    directory = parent_dir + "\\data\\"
    directories  = os.walk(directory)
    exp = ['mysql', 'performance_schema','phpmyadmin','test','']

    for d in directories:
        dir = d[0].rsplit("\\", 1)[-1]
        if(dir not in exp):
            shutil.copytree(parent_dir+"\\data\\"+dir, destination_folder+dir, symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=False)
            print("FROM : "+ parent_dir+"\\data\\"+dir + " To : " +destination_folder)

    shutil.copy(ibdata1, destination_folder)
    print("Copy ibdata1 : " + ibdata1)

    now = datetime.now()
    newBack = now.strftime("%Y%m%d%H%M%S")
    os.rename(parent_dir+"\\data\\",parent_dir+"\\data_"+newBack)
    print("rename data to  data_" + newBack )

    os.rename(parent_dir+"\\new_data\\",parent_dir+"\\data")
    print("rename new_data to data " )
    
def copyBackupDirs():
    shutil.copytree(source_folder, destination_folder, symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=False)
    print("createDataDir ... Done")
    copyDataDirs()

copyBackupDirs()




print("END")