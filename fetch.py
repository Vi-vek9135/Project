import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
# PARENT_FOLDER_ID = "1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL"

# def authenticate():
#     creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#     return creds


# def upload_file_to_drive(file_path):
#     creds = authenticate()
#     service = build('drive', 'v3', credentials=creds)

#     file_metadata = {
#         'name': "Hello",
#         'parents': [PARENT_FOLDER_ID]
#     }
#     file = service.files().create(body=file_metadata, media_body=file_path).execute()
    

# upload_file_to_drive("bharat_text.pdf")



service = Create_Service(SERVICE_ACCOUNT_FILE, 'drive', 'v3', SCOPES)
file_ids = ['1rFt_9jMOhwJuxfukeC02GUXgnVYIB5Tm']
file_names = ['test.pdf']

for file_id, file_name in zip(file_ids, file_names):
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print('Download progress {0}' .format(status.progress() * 100))
    fh.seek(0)
    with open(os.path.join('./Random Files',file_name), 'wb') as f:
        f.write(fh.read())
        f.close()
    fh.close()
    print(file_name, 'Downloaded')



    # I will be using the Google Drive API to download files from Google Drive. I have the file ID and the file name