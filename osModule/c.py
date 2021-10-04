import  os
from datetime import datetime
os.chdir("/Users/karth/Desktop")
# os.rename("demoDir3","demoDir4")
# it is used to change the name of the directory
# the name of the demoDir3 is changed to demoDir4

# print(os.stat("temp.txt"))
# stat will give the details of the file

# print(os.stat("temp.txt").st_dev)
# we can use the details using the dot notation

mod_time=os.stat("temp.txt").st_mtime
print(datetime.fromtimestamp(mod_time))

