import os
import os.path
import shutil
from datetime import datetime

def makefilename(filename):
    now = datetime.now()
    datestring = now.strftime('')
    filename = filename + '-' + datestring
    return filename

n = makefilename('test2.py')

backupdir = "/home/ec2-user/environment/backups"

source = r"/home/ec2-user/environment/test2.py"

target = r'/home/ec2-user/environment/backups/test2.py'

if os.path.exists(backupdir):
    shutil.copyfile(source, target)
    
else:
    
    os.mkdir(backupdir)
    shutil.copyfile(source, target)
    