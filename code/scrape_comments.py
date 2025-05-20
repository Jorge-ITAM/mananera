import os
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build
load_dotenv()
API_KEY = os.getenv("API_KEY")
youtube = build("youtube", "v3", developerKey=API_KEY)
def get_mananera_info(channel_id, max_results=5):
    response = youtube.search().list(
        q="#MañaneraDelPueblo",
        channelId=channel_id,
        part="snippet",
        order="date",
        maxResults=max_results,
        type="video"
    ).execute()
    video_info = []
    for item in response["items"]:
        video_info.append({
            "video_id": item["id"]["videoId"],
            "video_title": item["snippet"]["title"]
        })
    return video_info
def get_comments(video_id, max_comments=1000):
    comments = []
    next_page_token = None
    while len(comments) < max_comments:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token,
            textFormat="plainText"
        )
        response = request.execute()
        for item in response.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "video_id": video_id,
                "comment_id": item["id"],
                "author_id": snippet.get("authorChannelId", {}).get("value", "NA"),
                "author_name": snippet.get("authorDisplayName", "NA"),
                "comment_text": snippet.get("textDisplay", "NA"),
                "published_at": snippet.get("publishedAt", "NA")
            })
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break
    return comments
CHANNEL_ID = "UCvzHrtf9by1-UY67SfZse8w"
video_info_list = get_mananera_info(CHANNEL_ID, max_results=5)
all_comments = []
for video in video_info_list:
    vid = video["video_id"]
    title = video["video_title"]
    comments = get_comments(vid, max_comments=200)
    for c in comments:
        c["video_title"] = title
    all_comments.extend(comments)
df = pd.DataFrame(all_comments)
df.to_csv("../data/comments.csv")