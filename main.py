from youtube_stat import YT_Stat

API_KEY = 'AIzaSyALOUc6uuh9WW75Alh0hI4kFIEyTwE8s_Y'

channel_id = 'UCbXgNpp0jedKWcQiULLbDTA'

yt = YT_Stat(API_KEY,channel_id)

yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()
