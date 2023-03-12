from class_video import Video


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        youtube = self.get_service()
        self.playlist_id = youtube.playlists().list(id=playlist_id, part='snippet').execute()
        self.playlist_name = self.playlist_id['items'][0]['snippet']['title']

    def __str__(self):
        return f'{self.title} ({self.playlist_name})'
