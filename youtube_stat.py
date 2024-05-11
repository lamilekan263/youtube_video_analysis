import requests
import json

class YT_Stat:
    def __init__(self,api_key: str,channel_id:str):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        self.video_data = None

    def get_channel_statistics(self):
        url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)

        try:
            data = data['items'][0]['statistics']
        except:
            data = None

        self.channel_statistics = data
        return data
    
    def get_channel_video_data(self):
        channel_videos  = self._get_channel_videos(limit=50)
        print(channel_videos)

    def _get_channel_videos(self, limit=None):
        url = f"https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=id&order=date"
        if limit is not None and isinstance(limit, int):
            url += '&maxResults' + str(limit)

        vid, npt = self._get_channel_videos_per_page(url)
        idx = 0
        while(npt is not None and idx < 10):
            next_url = url + "&pageToken="+npt
            next_vid, npt = self._get_channel_videos_per_page(next_url)
            vid.update(next_vid)
            idx += 1
        return vid
    
    def _get_channel_videos_per_page(self,url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        channel_videos = dict()
        if 'items' not in data:
            return channel_videos, None
        item_data = data['items']
        next_page_token = data.get('nextPageToken', None)

        for item in item_data:
            try:
                kind = item['id']['kind']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    channel_videos[video_id] = dict()
            except KeyError:
                print("error")
        return channel_videos,next_page_token

    def dump(self):
        if self.channel_statistics == None:
            return
        channel_title = 'Python Engineer'
        channel_title = channel_title.replace(" ", '_').lower()
        file_name = channel_title +'.json'
        with open(file_name,'w') as f:
            json.dump(self.channel_statistics,f, indent=4)
        print('file dumped')