import os
import google
import google.auth
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# set up credentials
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file(
        'token.json', ['https://www.googleapis.com/auth/youtube.readonly'])
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(google.auth.transport.requests.Request())
    else:
        flow = google.auth.OAuth2FlowFromClientSecrets(
            'client_secret.json', ['https://www.googleapis.com/auth/youtube.readonly'])
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# set up YouTube API client
youtube = build('youtube', 'v3', credentials=creds)

# use YouTube API to search for a video
search_response = youtube.search().list(
    q='rick roll',
    type='video',
    part='id,snippet',
    maxResults=1
).execute()

# extract video ID from search response
video_id = search_response['items'][0]['id']['videoId']
print(f'Found video with ID: {video_id}')
