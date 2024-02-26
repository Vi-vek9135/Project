import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# folder = '1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL'


# # Download files
# file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
# for index, file in enumerate(file_list):
# 	print(index+1, 'file downloaded : ', file['title'])
# 	file.GetContentFile(file['title'])




# def get_file_list(folder_id):
#     gauth = GoogleAuth()
#     drive = GoogleDrive(gauth)

#     # Download files
#     file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
#     return file_list
	


from llama_index.readers.google import GoogleDriveReader
# from llama_index.readers.google import GoogleDriveReader

loader = GoogleDriveReader()
def load_data(folder_id: str):
	docs = loader.load_data(folder_id=folder_id)
	# for doc in docs:
	# 	doc.id_ = doc.metadata["file_name"]
		# doc.id_ = doc.metadata["bharat_text"]
	return docs


docs = load_data(folder_id="1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL")
print(docs)