from datetime import datetime, timedelta
import isodate

from class_mixin_service import MixinService


class PlayList(MixinService):

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        youtube = self.get_service()
        self.playlist = youtube.playlists().list(id=playlist_id, part='snippet').execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + playlist_id
        self.playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails', maxResults=50,).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = youtube.videos().list(part='contentDetails,statistics', id=','.join(self.video_ids)).execute()

    @property
    def total_duration(self):
        total_duration = timedelta()
        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def most_popular_video(self):
        max_like = 0
        for video in self.video_response['items']:
            if int(video['statistics']['likeCount']) > max_like:
                max_like = int(video['statistics']['likeCount'])
        for video in self.video_response['items']:
            if video['statistics']['likeCount'] == str(max_like):
                return f"https://www.youtube.com/watch?v={video['id']}"




pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')

print(pl.title)

print(pl.url)

duration = pl.total_duration
print(duration)
print(type(duration))
print(duration.total_seconds())
print(pl.most_popular_video())