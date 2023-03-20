import os
from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        try:
            youtube = self.get_service()
            self.video_response = youtube.videos().list(part='snippet,statistics', id=video_id).execute()
            self.title = self.video_response['items'][0]['snippet']['title']
            self.view_count = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count = self.video_response['items'][0]['statistics']['likeCount']

        except Exception:
            self.video_response = None
            self.title = None
            self.view_count = None
            self.like_count = None


    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def __str__(self):
        try:
            if self.title is not None:
                return self.title
            else:
                raise TypeError
        except TypeError:
            return f'Невозможно получить данные по этому IDшнику'

video1 = Video('broken_video_id')

print(video1)
print(video1.title)
print(video1.like_count)

