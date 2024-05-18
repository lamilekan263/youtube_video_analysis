from youtube_stat import YT_Stat
import os
from dotenv import load_dotenv



load_dotenv()
API_KEY = os.getenv('API_KEY')
channel_id = os.getenv('channel_id')

yt = YT_Stat(API_KEY,channel_id)

yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()
