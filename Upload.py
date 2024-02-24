import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL'

# file1 = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : 'hello2.txt'})
# file1.SetContentString('Hello world!, this is my second file')
# file1.Upload()





# Upload files
directory = "D:/Vivek_Roushan/docs"

for f in os.listdir(directory):
	filename = os.path.join(directory, f)
	gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
	gfile.SetContentFile(filename)
	gfile.Upload()