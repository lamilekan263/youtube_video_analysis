

class YT_Stat:
    def __init__(self,api_key: str,channel_id:str):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None

    def get_channel_statistics(self):
        url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}"
        print(url)