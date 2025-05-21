import os
import pandas as pd
from dotenv import load_dotenv
from utils import init_youtube, get_mananera_info, get_comments
# Cargar datos necesarios
load_dotenv()
API_KEY = os.getenv("API_KEY")
CHANNEL_ID = "UCvzHrtf9by1-UY67SfZse8w"
# Inicializar API
youtube = init_youtube(API_KEY)
# Webscraping
if __name__ == "__main__":
    video_info_list = get_mananera_info(youtube, CHANNEL_ID, max_results=5)

    all_comments = []
    for video in video_info_list:
        vid = video["video_id"]
        title = video["video_title"]
        comments = get_comments(youtube, vid, max_comments=200)
        for c in comments:
            c["video_title"] = title
        all_comments.extend(comments)

    df = pd.DataFrame(all_comments)
    df.to_csv("../data/comments.csv", index=False)
