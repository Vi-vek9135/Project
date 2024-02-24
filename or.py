"""
Copyright 2022 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# [START drive_download_file]

import os
# import io
from Google import Create_Service
# from googleapiclient.http import MediaIoBaseDownload

# from googleapiclient.discovery import build
from google.oauth2 import service_account
import io

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'


def download_file(real_file_id):
  """Downloads a file
  Args:
      real_file_id: ID of the file to download
  Returns : IO object with location.

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
#   creds, _ = google.auth.default()

  try:
    # create drive api client
    # service = build("drive", "v3", credentials=creds)
    service = build(SERVICE_ACCOUNT_FILE, 'drive', 'v3', credentials=SCOPES)

    file_id = real_file_id

    # pylint: disable=maybe-no-member
    request = service.files().get_media(fileId=file_id)
    file = io.BytesIO()
    downloader = MediaIoBaseDownload(file, request)
    done = False
    while done is False:
      status, done = downloader.next_chunk()
      print(f"Download {int(status.progress() * 100)}.")

  except HttpError as error:
    print(f"An error occurred: {error}")
    file = None

  return file.getvalue()


if __name__ == "__main__":
  download_file(real_file_id="1rFt_9jMOhwJuxfukeC02GUXgnVYIB5Tm")
# [END drive_download_file]